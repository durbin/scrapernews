from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from hackernews.spiders import *


class Command(BaseCommand):
    help = 'Scrape Hacker News Items'


    def handle(self, *args, **options):

        process = CrawlerProcess()
        process.crawl(ItemsSpider)
        process.start()

