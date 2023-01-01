import scrapy
from scrapy.loader import ItemLoader
from gov_data_singapore.items import GovDataSingaporeItem


BASE_URL = "https://data.gov.sg/dataset?page="


class AllDataSpider(scrapy.Spider):
    name = "all_data"
    allowed_domains = ["data.gov.sg"]

    start_urls = [BASE_URL + f"{i+1}" for i in range(50)]

    def parse(self, response):
        dataset_url = response.css(".col-12 h3 a::attr(href)")
        yield from response.follow_all(dataset_url, callback=self.parse_each)

    def parse_each(self, response):
        table_url = response.url
        url_selector = response.css("a.ga-dataset-download::attr(href)")
        loader = ItemLoader(item=GovDataSingaporeItem(), selector=url_selector)
        absolute_url = response.urljoin(url_selector.get())
        filename = response.css("h2.package-title::text").get()
        loader.add_value("file_urls", absolute_url)
        loader.add_value("file_name", filename)
        loader.add_value("table_url", table_url)
        yield loader.load_item()
