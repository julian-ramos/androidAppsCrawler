'''
Set of functions for the androidAppsCrawler
'''
import urllib.request as urllib2
from bs4 import BeautifulSoup


def appCategory(appName):
    '''
    This function returns the category of an app according to the
    android apps store
    AppName should be the app id which looks something like
    com.app.something
    '''
    response = urllib2.urlopen("https://play.google.com/store/apps/details?id="+appName)
    page_source = response.read()
    source_string=str(page_source)
    ind=source_string.find('<a class="document-subtitle category"')
    ind2=source_string[ind:-1].find('href="')
    ind3=source_string[ind+ind2:-1].find('">')
    category=source_string[ind+ind2+6:ind+ind2+ind3]
    category=category.split('/')[-1]
    return category
    
    
    
    
    