# Task-1: Doing Http request to a URL and doing HTML parsing using BeautifulSoup --> Storing in the txt document file
from bs4 import BeautifulSoup
import requests

page_link = 'https://en.wikipedia.org/wiki/Google'
page_response = requests.get(page_link)

page_content = BeautifulSoup(page_response.content, "html.parser")
text = page_content.get_text()


# Task-2: Storing the text output to a file
with open('output.txt', 'w',encoding='utf-8') as f:
    f.write(text)