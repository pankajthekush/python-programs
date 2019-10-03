# -*- coding: utf-8 -*-
import scrapy


class CrawlpageSpider(scrapy.Spider):
    name = 'crawlpage'
    allowed_domains = ['web']
    #start_urls = []
   
    def parse(self, response):
        page = response.text
        filename = 'output.html'
        with open(filename, 'ab') as f:
            f.write(response.body)
     




