# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
import time


class CrawlpageSpider(scrapy.Spider):
    name = 'crawlpage'
    allowed_domains = ['nytimes.com']


    def parse(self, response):
        page = response.text
        filename = 'output.html'
        with open(filename, 'ab') as f:
            f.write(response.body)
       