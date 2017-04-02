'''
A script to get the related Articles on Baidu Baike , after you type in any valid Arctice
'''


from urllib.parse import unquote

from urllib.request import urlopen

from bs4 import BeautifulSoup

import re


def getLinks(itemUrl):
    html = urlopen(itemUrl)
    bs4obj = BeautifulSoup(html, "html.parser")
    return bs4obj.find("div", {"class": "main-content"}).findAll("a", href=re.compile("^(/item/)."))


item = input("Please enter any article exists on Baike: \n")
itemUrl = "http://baike.baidu.com/item/" + item
links = getLinks(itemUrl)
print("Got it! It wil take a few seconds to get the reply...")
for link in links:
    print(unquote(link.attrs["href"])[6:])
