from typing import Iterable

import scrapy
from scrapy import Request


class PwspiderSpider(scrapy.Spider):
    name = "pwspider"

    def start_requests(self):
        yield scrapy.Request('https://shoppable-campaign-demo.netlify.app/#/',
                             meta={'playwright': True})

    def parse(self, response):
        yield {
            'text': response.text
        }
