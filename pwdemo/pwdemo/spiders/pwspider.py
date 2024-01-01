import scrapy
from scrapy_playwright.page import PageMethod
from scrapy import Request


class PwspiderSpider(scrapy.Spider):
    name = "pwspider"

    def start_requests(self):
        yield scrapy.Request('https://shoppable-campaign-demo.netlify.app/#/',
                             meta=dict(
                                 playwright=True,
                                 playwright_include_page=True,
                                 playwright_page_coroutines=[
                                     PageMethod('wait_for_selector', 'div#productListing')
                                 ]
                             ))

    async def parse(self, response):
        for product in response.css('div.card-body'):
            yield {
                'title': product.css('h3::text').get(),
                'price': product.css('div.form-group label::text').get(),
            }
