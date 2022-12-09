import requests
import bs4
import xml.etree.ElementTree as ET

def download(url: str, name: str):
    f = open(name, 'wb')
    f.write(requests.get(url).content)

# auth_url = 'https://sso.bmstu.com/auth/?return_path=https%253A%252F%252Fsso.bmstu.com%252Foauth%252Fauthorization_code%252F&auth_request_key=oAuthRequest'
session = requests.Session()
header = {
    'user-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/5.0)',
    'Cookie': ''
}
book_url = 'https://bmstu.press/catalog/item/6861/'
book_cover = session.get(book_url+'/reader/', headers=header).text

parsed_book_cover = bs4.BeautifulSoup(book_cover, 'lxml')
files_path = parsed_book_cover.find('div', id='app-reader').find('app-reader')['url']
download(files_path, 'data.opf')

tree = ET.parse('data.opf')
root = tree.getroot()
print(root[0].find("{http://purl.org/dc/elements/1.1/}title").text)



# num = 1
# pdfs = []
# merger = PdfFileMerger()
# while True:
#     page_num = '{0:0>4}'.format(num)
#     try:
#         reader = parsed_book_cover.find('div', id='app-reader').find('app-reader')['url'][0:-11]+'mybook' + page_num + '.xhtml'
#         if requests.get(reader).headers['content-type'] == 'text/html; charset=utf-8':
#             raise
#         print(reader)
#         pdfkit.from_url(reader, 'files/'+page_num+'.pdf', options={'page-size':'A5'})
#         merger.append('files/'+page_num+'.pdf')
#         num = num + 1
#     except:
#         print('Download finished! last page is', int(page_num)-1)
#         break
# print('Merging...')
# merger.write('out.pdf')
# merger.close()
