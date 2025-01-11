import requests
from lxml import etree

url1 = input('请输入歌单链接：')
url = url1[:22]+url1[24:]
print(url)
base_url = 'https://music.163.com/song/media/outer/url?id='

ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}

html_str = requests.get(url,headers=ua).text
html_dom = etree.HTML(html_str)

song_names = html_dom.xpath('//a[contains(@href,"song?")]/text()')
song_ids = html_dom.xpath('//a[contains(@href,"song?")]/@href')

for song_name,song_id in zip(song_names,song_ids):
    song_idid = song_id.strip('/song?id=')
    if ('$' in song_idid)==False:
        song_url = base_url + song_idid
        if ('#/wiki')
        print(song_url)
        m4a = requests.get(song_url,headers=ua).content

        with open('./py实例/wyymusic/%s.mp3'%song_name,'wb') as file:
            file.write(m4a)



