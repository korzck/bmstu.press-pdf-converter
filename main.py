import requests

url = 'http://bmstu.press/'

proxies = { 'https' : 'https://user:password@proxy.bmstu.ru:8476' }
r = requests.get(url, proxies=proxies) 

print(r.text)
