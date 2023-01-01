# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import os


# class GovDataSingaporePipeline(FilesPipeline):
#     def get_media_requests(self, item, info):
#         urls = ItemAdapter(item).get(self.files_urls_field, [])
#         filename = item.get("file_name")[0].replace(",", "").replace(" ", "_")
#         return [Request(u, meta={"filename": filename}) for u in urls]

#     def file_path(self, request, response=None, info=None, *, item=None):
#         filename = request.meta["filename"]
#         return f"{filename}.zip"


class GovDataSingaporePipeline:
    def process_item(self, item, spider):
        return item
