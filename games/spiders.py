import scrapy


class StopGameSpider(scrapy.Spider):
    name = "stopgame.ru"
    start_urls = ["https://stopgame.ru/games/filter?year_start=2020&year_end=2021"]

    def parse(self, response, **kwargs):
        for game in response.css(".games-list .item"):
            try:
                stopgame_rating = game.css(".score .value::text").get().strip()
            except Exception:
                stopgame_rating = 0

            data = {
                "name": game.css(".caption a::text").get(),
                "stopgame_rating": stopgame_rating,
                "stopgame_link": f'https://stopgame.ru{game.css(".caption a::attr(href)").get()}',
            }
            yield data

        next_page = response.css(
            "._container_twrvg_1 a.next:last-child::attr(href)"
        ).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
