import requests
from bs4 import BeautifulSoup

#get the content from URL given
getHTML= requests.get('https://scikit-learn.org/stable/modules/clustering.html#clustering')
#scrapping website using BeautifulSoup
getParsedHTML= BeautifulSoup(getHTML.text, "html.parser")
getTable = getParsedHTML.find('table')
#get headings from table
headings = getTable.find("thead")
# print(headings)
for heading in headings:
    tableHeading = headings.find_all('th')
    tableHeading=[ele.text.strip() for ele in tableHeading]
print(tableHeading)


getContent = getTable.find_all('tr')
for eachRow in getContent:
    contents = eachRow.find_all('td')
    contents = [ele.text.strip() for ele in contents]
    print(contents)
