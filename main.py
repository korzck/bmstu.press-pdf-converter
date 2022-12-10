import requests
import bs4
import xml.etree.ElementTree as ET

def download(url: str, path: str):
    f = open(path, 'wb')
    f.write(requests.get(url).content)

# auth_url = 'https://sso.bmstu.com/auth/?return_path=https%253A%252F%252Fsso.bmstu.com%252Foauth%252Fauthorization_code%252F&auth_request_key=oAuthRequest'
session = requests.Session()
header = {
    'user-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/5.0)',
    'Cookie': ''
}
book_url = 'https://bmstu.press/catalog/item/6864/'
book_cover = session.get(book_url+'/reader/', headers=header).text

parsed_book_cover = bs4.BeautifulSoup(book_cover, 'lxml')
files_path = parsed_book_cover.find('div', id='app-reader').find('app-reader')['url']
download(files_path, 'data.opf')
#trimm the url
files_path = files_path[0:-11]

tree = ET.parse('data.opf')
root = tree.getroot()
book_name = root[0].find("{http://purl.org/dc/elements/1.1/}title").text

upper = f'''
<html xmlns:epub="http://www.idpf.org/2007/ops" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="UTF-8"/>
  <meta name="" content=""/>
  <link rel="stylesheet" type="text/css" href="base.min.css"/>
  <link rel="stylesheet" type="text/css" href="mybook.css"/>
  <meta name="viewport" content="width=900, height=1281"/>
  <title>{book_name}</title>
</head>
<body>
<div id="page-container">'''

lower = '''
</div>
</body>
</html>'''

f = open('files/index.xhtml', 'w')
f.write(upper)
for i in root[1]:
    print('Downloading', i.attrib['href'])
    download(files_path+i.attrib['href'], 'files/'+i.attrib['href'])
    if 'xhtml' in i.attrib['href']:
        content = open('files/'+i.attrib['href'], 'r')
        content = content.readlines()[12]
        f.write(content)
f.write(lower)
