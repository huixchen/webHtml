import re

import pymysql
import requests
from bs4 import BeautifulSoup

url = "https://book.douban.com/"

def connect():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='doubandb',
        charset='utf8',
    )
    return conn
def content(url):
    content = requests.get(url).text
    return content


def result(content, conn):
    cur = conn.cursor()
    soup = BeautifulSoup(content, "lxml")
    ulLadel = soup.find_all("ul", attrs={"class": "list-col list-col5 list-express slide-item"})
    bookList = []
    for ul in ulLadel:
        bookInfo = ul.find_all('div', attrs={'class': 'info'})
        for info in bookInfo:
            bookinfo = []
            # bookDict = {}
            # bookDict["bookUrl"] = info.find('a').get('href')
            # bookDict["bookName"] = info.find('a').get('title')
            # bookDict["bookAuthor"] = re.sub('\s', '', info.find('span', attrs={'class': 'author'}).string)
            # bookDict["bookYear"] = re.sub('\s', '', info.find('span', attrs={'class': 'year'}).string)
            # bookDict["bookPublisher"] = re.sub('\s', '', info.find('span', attrs={'class': 'publisher'}).string)
            # bookDict["bookAbstract"] = re.sub('\s', '', info.find('p', attrs={'class': 'abstract'}).string)
            # bookList.append(bookDict)

            bookUrl = info.find('a').get('href')
            bookName = info.find('a').get('title')
            bookAuthor = re.sub('\s', '', info.find('span', attrs={'class': 'author'}).string)
            bookYear = re.sub('\s', '', info.find('span', attrs={'class': 'year'}).string)
            bookPublisher = re.sub('\s', '', info.find('span', attrs={'class': 'publisher'}).string)
            bookAbstract = re.sub('\s', '', info.find('p', attrs={'class': 'abstract'}).string)

            bookinfo.append(bookUrl)
            bookinfo.append(bookName)
            bookinfo.append(bookAuthor)
            bookinfo.append(bookYear)
            bookinfo.append(bookPublisher)
            bookinfo.append(bookAbstract)
            bookList.append(bookinfo)
    cur.executemany('insert into book(bookUrl, bookName, bookAuthor, bookYear, bookPublisher, bookAbstract) VALUES(%s, %s, %s,%s,%s,%s) ', bookList)
    cur.close()
    conn.commit()
    conn.close()
    # print(bookDict)
def main():
    conn = connect()
    rest = content(url)
    result(rest, conn)


if __name__ == '__main__':
    main()
    print("Done!")

