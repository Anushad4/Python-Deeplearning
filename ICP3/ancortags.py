import requests
from bs4 import BeautifulSoup

#getting the web content
html_doc = requests.get('https://en.wikipedia.org/wiki/Deep_learning')

#scrapping content using BeautifulSoup #html parser to encounter the tags and text
soup = BeautifulSoup(html_doc.text,'html.parser')
title = soup.title.string
print("title of a page:",title)
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

print("len of links",len(links))

#write in a file
with open('webscraping.txt', 'w') as f:
    f.write("Title: " + title + "\n")
    f.write("Links: " + "\n")
    for link in links:
        f.write("Link: " + str(link) + "\n")

print("webscraping text is created and data is stored")