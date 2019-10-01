from bs4 import BeautifulSoup
from bs4.element import Comment
import re



def tagmaps(element):
    avoid_list = ['style', 'script', 'head', 'title', 'meta', '[document]']
    if element.parent.name  in avoid_list:
        return False
    if isinstance(element,Comment):
        return False
    else:
        return True

def cleantagtext(tagtext):
    visibletext = filter(tagmaps,tagtext)
    speechtext = " ".join(t.strip() for t in visibletext)
    return speechtext

def removewhitespace(intext):
    retext = intext.replace('\r','').replace('\n','')
    return retext

def removespecial(intext):
    rettext = intext.replace('.', ' ')
    return rettext

def removefromfile(intext):
    
    file = open('avoidwords',"r") 
    words = intext.split(' ')
    rawdata = file.read()
    ldata = rawdata.split(',')

    for badword in ldata:
        if badword in words:
            words = [t  for t in words if t != badword]
    
    intext = ' '.join(t.strip() for t in words)
    
    return intext

def removesinglechar(intext):
    return intext
    

