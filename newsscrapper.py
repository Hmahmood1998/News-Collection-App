import requests
from bs4 import BeautifulSoup 



def newsNDTV():
    url="https://www.ndtv.com/top-stories"
    data=requests.get(url)
    soup=BeautifulSoup(data.text)

    news = []
    for row in soup.find_all('div',{'class':'news_Itm'}):
        detail = {}
        if not  'adBg' in row.attrs.get('class'):
            
            detail['link'] = row.find('h2').attrs.get('href')
            detail['heading'] = row.find('h2')
            
            detail['src']=row.find('span').text
            
            detail['summary']=row.find('p').text
            
            detail['image']=row.find('img').attrs.get('src')
            
        news.append(detail)
    return news