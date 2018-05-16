import re 
import requests 
from bs4 import BeautifulSoup 
import urllib
 
 
def get_image(query): 
    chart_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' +urllib.parse.quote_plus(query)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    html = requests.get(chart_url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser') 

    tag = soup.find(attrs={'class':"_img"})
    return tag['data-source']
 
if __name__ == '__main__': 
     get_image()

