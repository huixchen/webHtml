# from bs4 import BeautifulSoup
#
# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <span class="author">好好住</span>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print("--------------------------")
# print(soup.title)
# print("--------------------------")
# print(soup.title.name)
# print("--------------------------")
# print(soup.title.string)
# print("--------------------------")
# print(soup.title.parent.name)
# print("--------------------------")
# print(soup.span.string)
# print("--------------------------")
# print(soup.find_all('p'))
# print("--------------------------")
# print("srint  "+soup.p.string)
# print("--------------------------")
# print(soup.a)
# print("--------------------------")
# print(soup.find_all('a'))
# print("--------------------------")
# print(soup.find(id='link3'))

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('#container .list li'))
