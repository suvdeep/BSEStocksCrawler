import scrapy
from rediff_stocks.items import RediffStocksItem


class StockGainers(scrapy.Spider):
    """docstring for StockGainers"""
    name = "rediff"
    allowed_domains = ["rediff.com"]
    start_urls = ["http://money.rediff.com/gainers/bse/daily/groupa", ]

    def parse(self, response):
        for sel in response.xpath("/html/body/div[1]/div[5]/table/tbody/tr"):
            item = RediffStocksItem()
            item['company'] = sel.xpath("td[1]/a/text()")[0].extract().strip()
            item['price'] = sel.xpath("td[4]/text()")[0].extract()
            item['change'] = sel.xpath("td[5]/font/text()")[0].extract()
            yield item
