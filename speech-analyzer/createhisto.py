import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from cleantext import *
from processing import createhistogram,showhistogram
from collections import Counter

class GetSpeech():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
    def getfromurl(self,url):

        session = requests.Session()
        response = session.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        alltext = soup.find_all(text=True)
        alltext = cleantagtext(alltext)
        speechtext = removewhitespace(alltext)
        speechtext = removespecial(speechtext)
        speechtext = removefromfile(speechtext)
        speechtext = removesinglechar(speechtext)
        return speechtext

if __name__ == '__main__':
    cs = GetSpeech()
    text  = cs.getfromurl(url='http://www.worldfuturefund.org/Articles/Hitler/hitler1939.html')
    histo = createhistogram(text)
    histo = Counter(histo)
    toptwenty = histo.most_common(20)
    toptwenty = dict(toptwenty)
    print(toptwenty)
    showhistogram(toptwenty)
    #print(histo)