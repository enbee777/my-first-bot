from __future__ import unicode_literals 
import re 
import requests 
from bs4 import BeautifulSoup 
 
 
 
 
def melon_chart(): 
    chart_url = 'http://www.melon.com/chart/index.htm' 
    html = requests.get(chart_url).text 
    soup = BeautifulSoup(html, 'html.parser') 
    for idx, song_tag in enumerate(soup.select('#chartListObj .lst50 a[href*=playSong]'), 1): 
        menu_id, song_id = re.findall(r'\d+', song_tag['href']) 
        song_url = 'http://www.melon.com/song/detail.htm?songId=' + song_id 
        print(idx, song_tag.text, '||', song_url) 
 
 
 
 
if __name__ == '__main__': 
     melon_chart() 
