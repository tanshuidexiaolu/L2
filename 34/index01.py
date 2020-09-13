import requests, os
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome56.0.2924.87 Safari/537.36'}
url = 'https://music.douban.com/tag/民谣'
response = requests.get(url,headers=headers)
os.system("start "+response.url)
