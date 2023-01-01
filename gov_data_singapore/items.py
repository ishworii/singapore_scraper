# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.pipelines.files import FilesPipeline


class GovDataSingaporeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_urls = scrapy.Field()
    file_name = scrapy.Field()
    files = scrapy.Field()
    table_url = scrapy.Field()
