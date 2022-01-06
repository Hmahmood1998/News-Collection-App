import requests
from bs4 import BeautifulSoup


def newsNDTV():
    url = "https://www.ndtv.com/top-stories"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)

    news = []
    for row in soup.find_all('div', {'class': 'news_Itm'}):
        detail = {}
        if not 'adBg' in row.attrs.get('class'):

            detail['heading'] = row.find('h2').text
            detail['src'] = row.find('span').text
            detail['summary'] = row.find('p').text
            detail['link'] = row.find('h2').find('a').attrs.get('href')
            detail['image'] = row.find('img').attrs.get('src')

        news.append(detail)
    return news


def IndiaToday():
    url = "https://www.indiatoday.in/top-stories"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)

    news = []
    for row in soup.find_all('div', {'class': 'catagory-listing'}):
        detail = {}

        detail['heading'] = row.find('h2').text
        detail['summary'] = row.find('p').text
        detail['link'] = row.find('h2').find('a').attrs.get('href')
        # detail['image']=row.find('pic').attrs.get('src')

        news.append(detail)
    return news


def IndianExpress():
    url = "https://indianexpress.com/latest-news/"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)

    
    news=[]
    for row in soup.find_all('div',{'class':'articles'}):
        detail={}
        
        detail['src'] = row.find('div').text
        detail['summary']=row.find('p').text
        detail['link'] = row.find('a').attrs.get('href')
        detail['image'] = row.find('img').attrs.get('src')

    news.append(detail)


def BusinessStandard():
    url = "https://www.business-standard.com/most-read/list/day/relevance"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)

    news = []
    for row in soup.find_all('div', {'class': 'articles'}):
        detail = {}
        detail['sourse'] = row.find('div')
        detail['summary'] = row.find('p').text
        detail['link'] = row.find('a').attrs.get('href')
        detail['image'] = row.find('img').attrs.get('src')

        news.append(detail)



def News18():
    url="https://www.news18.com/"
    data=requests.get(url)
    soup=BeautifulSoup(data.text)

    news=[]
    for row in soup.find_all('li',{'class':'fnt-siz-e'}):
        detail={}





