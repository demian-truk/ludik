from django.core.management import BaseCommand
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from games.models import Game
from games.spiders import StopGameSpider


class Command(BaseCommand):
    help = "Crawl StopGame games list"

    def handle(self, *args, **options):
        def crawler_results(signal, sender, item, response, spider):
            Game.objects.update_or_create(
                stopgame_link=item["stopgame_link"], defaults=item
            )

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(StopGameSpider)
        process.start()
