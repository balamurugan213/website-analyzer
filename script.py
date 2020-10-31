# from flask import Flask
from flask import *
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
# 
@app.route('/')

 """Return the sum of x and y.""" 
def home():
    return render_template('index.html')  

# def about():  
#     return 'app'
# app.add_url_rule("/about", "about", about)

  
@app.route('/admin',methods = ['POST'])
def admin():
    url=request.form['uname']
    try:
        response = requests.get(url) 
        src = response.content
        soup = BeautifulSoup(src, 'xml')
        links = soup.find_all("h3")
        for link in links:
            print(link.attrs)
            print("\n")
        return render_template("result.html", links=links,flag1=1)
    except:
        links="some thing went wrong try again"
        return render_template("result.html", links=links,flag1=0)
  
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
