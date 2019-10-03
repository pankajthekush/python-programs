import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from cleantext import *
from histoprocess import createhistogram,showhistogram
from collections import Counter
from scrapy.crawler import CrawlerProcess
from scrapepages.scrapepages.spiders.crawlpage import CrawlpageSpider

class GetSpeech():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
    def getfromurl(self,url):

        process = CrawlerProcess()
        process.crawl(CrawlpageSpider,start_urls=url)
        process.start()
        
        page = open('output.html', encoding='utf8')

        soup = BeautifulSoup(page.read(),'html.parser')

        alltext = soup.find_all(text=True)
        alltext = cleantagtext(alltext)
        speechtext = removewhitespace(alltext)
        speechtext = removefromfile(speechtext)
    
        return speechtext

if __name__ == '__main__':
    
    cs = GetSpeech()
    text  = cs.getfromurl(url=['https://webscraper.io/test-sites/e-commerce/allinone'])
    histo = createhistogram(text)
    histo = Counter(histo)
    toptwenty = histo.most_common(10)
    toptwenty = dict(toptwenty)
    print(toptwenty)
    showhistogram(toptwenty)
    #print(histo)