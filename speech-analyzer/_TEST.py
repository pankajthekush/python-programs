from scrapy.crawler import CrawlerProcess
from scrapepages.scrapepages.spiders.crawlpage import CrawlpageSpider
from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy.signalmanager import dispatcher

def spider_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(CrawlpageSpider)
    process.start()  # the script will block here until the crawling is finished
    return results


if __name__ == '__main__':
    print(spider_results())