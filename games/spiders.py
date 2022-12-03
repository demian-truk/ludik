import scrapy


class StopGameSpider(scrapy.Spider):
    name = "stopgame.ru"
    allowed_domains = ["stopgame.ru"]
    start_urls = ["https://stopgame.ru/games/filter?year_start=2021&year_end=2021"]

    def parse(self, response, **kwargs):
        for game in response.css(".list-view ._card_67304_1"):
            stopgame_rating = game.css("._info-container_67304_30 button::text").get()
            stopgame_rating = (
                stopgame_rating.strip() if stopgame_rating is not None else 0
            )

            data = {
                "stopgame_rating": stopgame_rating,
                "stopgame_link": f'https://stopgame.ru{game.css("a::attr(href)").get()}',
            }
            yield data

        next_page = response.css("._container_1mcqg_1 .next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
