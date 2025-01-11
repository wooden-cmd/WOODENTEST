import requests

while True:
    msg =input('我:')
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={msg}'
    content = requests.get(url).json()['content'].replace('{br}','')
    print(content)