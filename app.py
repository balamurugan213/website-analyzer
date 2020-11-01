# from flask import Flask
from flask import *
import requests
from bs4 import BeautifulSoup
from Modules import web_scraper
from Modules import Nltk_module
import json

app = Flask(__name__)
# 
@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/admin',methods = ['POST'])
def admin():
    url=request.form['uname']
    try:
        print(url)
        soup=web_scraper.BeautifulSoupModule(url)
        response =soup.GetResponse()   
        li=soup.IsActiveCheck(response)
        print(li)
        # src = response.content
        # soup = BeautifulSoup(src, 'xml')
        # links = soup.find_all("h3")
        # for link in links:
        #     print(link.attrs)
        #     print("\n")
        # links=soup.GetAllLinks(response)
        # print(links)
        info=soup.firstInfo(response)
        print(info)
        print("\n")
        nav=soup.MainLinks(response)
        print(nav)
        print("\n")
        keywords=soup.GetAllHeadings(response)
        print(keywords)
        print("\n")
        img=soup.GetImgLinks(response)
        print(img)
        print("\n")
        links=soup.GetAllTextLink(response)
        print(links)
        print("\n")
        dis=soup.status
        print(dis)
        print("hpp")
        burl=soup.home_url
        # 
        bigrams=Nltk_module.BigramModule(keywords)
        # r=bigrams.FindBigrams()  
        r=bigrams.FindUnigrams()        
        print(r)
        return render_template("rs.html",burl=burl,info=info,nav=nav,links=links,ing=img ,dis=dis,flag1 = 1)
    except:
        img="some thing went wrong try again"
        return render_template("rs.html", img=img, flag1 = 1)
  
# @app.route('/librarion')
# def librarion():
#     return 'librarion'
  
# @app.route('/student')
# def student():
#     return 'student'
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    # if name == 'librarion':
    #     return redirect(url_for('librarion'))
    # if name == 'student':
    #     return redirect(url_for('student'))
if __name__ =='__main__':
    app.run(debug = True)
