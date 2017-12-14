import re

import requests

content = requests.get("https://book.douban.com/").text

pattern = re.compile('<li.*?"cover">.*?href="(.*?)".*?title="(.*?)">.*?"author">(.*?)<.*?"year">(.*?)<.*?"publisher">(.*?)<.*?li>', re.S)
#<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>
results = re.findall(pattern, content)
print(results)

for result in results:
    bookDict = {}
    url, bookName, author, year, publisher = result
    bookDict["bookUrl"] = re.sub('\s', '', url)
    bookDict["bookName"] = re.sub('\s', '', bookName)
    bookDict["bookAuthor"] = re.sub('\s', '', author)
    bookDict["bookYear"] = re.sub('\s', '', year)
    bookDict["publisher"] = re.sub('\s', '', publisher)

    print(bookDict)

