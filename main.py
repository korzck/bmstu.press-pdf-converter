import requests
import bs4


# auth_url = 'https://sso.bmstu.com/auth/?return_path=https%253A%252F%252Fsso.bmstu.com%252Foauth%252Fauthorization_code%252F&auth_request_key=oAuthRequest'
session = requests.Session()
header = {
    'user-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/5.0)',
    'Cookie': 'pase ur cookie here'
}

book_url = 'https://bmstu.press/catalog/item/6864/'

response = session.get(book_url+'/reader/', headers=header).text
f = open('index.html', 'w').write(response)
soup = bs4.BeautifulSoup(response, 'lxml')

try:
    reader = soup.find('div', id='app-reader').find('app-reader')['url'][0:-11]+'mybook0001.xhtml'
    print(reader)
except:
    print('bad page!')





