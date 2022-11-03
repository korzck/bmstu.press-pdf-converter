import requests
import bs4


# auth_url = 'https://sso.bmstu.com/auth/?return_path=https%253A%252F%252Fsso.bmstu.com%252Foauth%252Fauthorization_code%252F&auth_request_key=oAuthRequest'
session = requests.Session()
header = {
    'user-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/5.0)',
    'Cookie': 'pase ur cookie'
}

book_url = 'https://bmstu.press/catalog/item/6864/'

book_cover = session.get(book_url+'/reader/', headers=header).text
parsed_book_cover = bs4.BeautifulSoup(book_cover, 'lxml')



num = 1
while True:
    page_num = '{0:0>4}'.format(num)
    try:
        reader = parsed_book_cover.find('div', id='app-reader').find('app-reader')['url'][0:-11]+'mybook' + page_num + '.xhtml'
        if requests.get(reader).headers['content-type'] == 'text/html; charset=utf-8':
            raise
        print(reader)
        num = num + 1
    except:
        print('bad page! total pages', int(page_num)-1)
        break
