# bmstu.press pdf converter

Для использования необходимо вставить куки со страницы самой читалки из главного GET-запроса (например, страница https://bmstu.press/catalog/item/7187/reader/ является читалкой)


Скрипт собирает все файлы из opf-списка (https://bmstu.press/ebooks/xxxx/xx/xx/x/OEBPS/content.opf) и загружает их в папку `files` в той же директории, что и скрипт. После выполнения в папке `files` будет находится `index.html` - файл с объединенными div-контейнерами с контентом каждой страницы, который необходимо открыть в любом браузере и просто выполнить печать в pdf в формате А5 (возможно иногда А4).

Строка с куки должна выглядеть так: 
```python
header = {
    'user-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/5.0)',
    'Cookie': '__SECURE-PHPSESSID=12345; bmstu-press=12345; key=12345'
}
```

В переменную `book_url` необходимо записать строку в формате `'https://bmstu.press/catalog/item/1234/'`. 

### Авторские права не нарушены, разработчики этого скрипта не несут ответственности за чужие действия!

### No copyrights were violated, all developers of this script are not responsible for any actions of third parties!
