"""
This module of program is for web Scraping functionalities.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
import requests
from bs4 import BeautifulSoup
import json
import re

class BeautifulSoupModule:

    url=""
    home_url=''
    status={}

    def __init__(self,link):
        self.url = link
        x = re.findall("https?:\/\/.+.", self.url)
        self.home_url=x[0]
        # print("home url is")
        # print(self.home_url)

    def GetResponse(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(self.url, headers=headers)
        return response  
    
    def SoupObject(self,response):
        src = response.content.decode()
        soupObj = BeautifulSoup(src, 'lxml')
        return soupObj
    
    def IsActiveCheck(self, response):
        status=0
        value=0
        try:  
           status=1
           value=response.status_code
           print(value)
        except:
           status=1
           value=0
           print(value)
        finally:
            resp=[status,value]
            return resp
    
    def firstInfo(self,response):
        print("reando tes")
        info=[]
        # 
        soupa = self.SoupObject(response)
        title_tags = soupa.find("title")
        info.append(title_tags.string)
        # 
        try:
            print("reando te3s")
            if soupa.find("img", attrs={'class': re.compile("logo")}):
                logo_tags = soupa.find("img", attrs={'class': re.compile("logo")})
            else:
                logo_tags = soupa.find("img")
            print(logo_tags)
            logo=logo_tags['src']
            print("reando tes")
            print(logo_tags.parent)
            href=logo_tags.parent['href']
            info.append(logo)
            info.append(href)
            self.status['logo']=1
        except:
            self.status['logo']=0
        finally:
            return info
    
    def MainLinks(self,response):
        nav=[]
        try:
            soupa = self.SoupObject(response)
            # if soupa.find("nav"):
            nav_tags = soupa.find("nav")
            # print(nav_tags)
            nav_element = nav_tags.find_all("li")
            for element in nav_element:
                p=element.contents[0]
                if p.string:
                    nav.append({"href":p["href"],"text":p.string})
            self.status['nav']=1
        except:
            self.status['nav']=0
        # print(nav)
        return nav
    
    def GetAllLinks(self,response):
        soupa = self.SoupObject(response)
        links = soupa.find_all("a")
        return links
    
    def GetImgLinks(self,response):
        links=self.GetAllLinks(response)
        img_link=[]
        try:
            for link in links:
                if link.find('img'):
                    img_tag=link.find('img')
                    img_link.append({"href":link["href"],"src":img_tag["src"]})
            # print(img_link)
            self.status['img']=1
        except:
            self.status['img']=0
        return img_link
    
    def GetAllHeadings(self,response):
        # print("jojo")
        soupa = self.SoupObject(response)
        try:
            h1 = soupa.find_all(['h1','h2','h3','h4','p'])
            # print(h1)
            headings=[]
            for h in h1:
                if h.string:
                    headings.append(h.string)
            # print(headings)
            self.status['keyword']=1
        except:
            self.status['keyword']=0
        finally:
            return headings   

    def GetAllTextLink(self,response):
        try:
            links=self.GetAllLinks(response)
            img_link=[]
            for link in links:
                if link.string:
                    img_tag=link.find('img')
                    img_link.append({"href":link["href"],"text":link.string})
            # print(img_link)
            self.status['text']=1
        except:
            self.status['text']=0
        return img_link   