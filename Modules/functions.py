"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
import requests
from bs4 import BeautifulSoup
import re

class Soup:
    url=""
    home_url=''
    def __init__(self,link):
        print("fn is working mi")
        self.url = link
        # https?:\/\/.+.com
        x = re.findall("https?:\/\/.+.com", self.url)
        self.home_url=x[0]
        print("home url is")
        print(self.home_url)

    def GetResponse(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(self.url, headers=headers)
        return response
    
    def SoupObject(self,response):
        src = response.content.decode()
        soupObj = BeautifulSoup(src, 'lxml')
        return soupObj

    def IsActiveCheck(self, response):
        print("fn is working")
        # response = requests.get(self.url)
        status=0
        value=0
        print("fn is working 0")
        try:  
           print("fn is working1")
           status=1
           value=response.status_code
           print(value)
        except:
           print("fn is working2")
           status=1
           value=0
           print(value)
        finally:
            print("fn is working3")
            resp=[status,value]
            return resp

    def firstInfo(self,response):
        print("fffffffffffff")
        soupa = self.SoupObject(response)
        title = soupa.find("title")
        print(title.string)
        logo = soupa.find("img", attrs={'class': re.compile("logo")})
        print(logo.parent)
        nav = soupa.find("nav")
        nav_ele = nav.find_all("li")
        for nav2 in nav_ele:
            print(nav2.contents[0])
        # print(nav)
        return title
    
    def GetAllLinks(self,response):
        soupa = self.SoupObject(response)
        # print(soupa.prettify())
        links = soupa.find_all("a")
        # attrs={'href': re.compile("^http://")}
        print("Gggg")
        li=[]
        # print(links)
        for link in links:
            li.append(link.attrs)
            print(link.string)
            print(link.attrs)
            print("\n")
        return links

    def GetImgLinks(self,response):
        print("ggg")
        links=self.GetAllLinks(response)
        print("ale")
        img_link=[]
        for link in links:
            if link.find('img'):
                a=[]
                img=link.find('img')
                img_link.append({"href":link["href"],"src":img["src"]})
                a.append(link['href'])
                # img_link.append(a)
                print('\n')
        # print(img_link)
        return img_link

    def GetAllHeadings(self,response):
        print("jojo")
        soupa = self.SoupObject(response)
        h1 = soupa.find_all(['h1','h2','h3','h4','p'])
        print(h1)
        headings=[]
        for h in h1:
            headings.append(h.string)
        print(headings)
        return headings

    def GetAllKeywords(self,response):
        print("jojo")
        soupa = self.SoupObject(response)
        h1 = soupa.find_all('img')
        print(h1)
        keywords=[]
        print(keywords)
        return keywords
# try:
#     link = input() 
#     response = requests.get(link)
#     print(response.status_code)
#     # print(response.headers)
#     src = response.content
#     soup = BeautifulSoup(src, 'xml')
#     links = soup.find_all("a")
#     for link in links:
#         print(link.attrs)
#         print("\n")
#     # for link in links:
#     #     if "About" in link.text:
#     #         # print(link)
#     #         print(link.attrs['href'])
# except:
#     # print("give other link")
#     raise Exception("Invalid link")

