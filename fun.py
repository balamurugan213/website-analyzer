"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
import requests
from bs4 import BeautifulSoup

try:
    link = input() 
    response = requests.get(link)
    # print(response.status_code)
    # print(response.headers)
    src = response.content
    soup = BeautifulSoup(src, 'xml')
    links = soup.find_all("a")
    for link in links:
        print(link.attrs)
        print("\n")
    # for link in links:
    #     if "About" in link.text:
    #         # print(link)
    #         print(link.attrs['href'])
except:
    # print("give other link")
    raise Exception("Invalid link")

