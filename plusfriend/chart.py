from __future__ import unicode_literals 
import re 
import requests 
from bs4 import BeautifulSoup 
 
 
 
 
def melon_chart(): 
    chart_url = 'http://www.melon.com/chart/index.htm'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    html = requests.get(chart_url, headers=headers).text 
    soup = BeautifulSoup(html, 'html.parser') 
    res = ''
    for idx, song_tag in enumerate(soup.select('#frm a[href*=playSong]'), 1): 
        menu_id, song_id = re.findall(r'\d+', song_tag['href']) 
        song_url = 'http://www.melon.com/song/detail.htm?songId=' + song_id 
        res += '%d %s || %s\n'%(idx, song_tag.text, song_url) 
  
    return res
if __name__ == '__main__': 
     melon_chart() 
