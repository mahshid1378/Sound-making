import requests
from bs4 import BeautifulSoup

url = 'https://docs.cycling74.com/max8/tutorials/05_mspbasicchapter05'
# Using a different variable name for the response object
page_response = requests.get(url)
html_content = page_response.content
soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a')

for link in links:
    print(link.get('href'))