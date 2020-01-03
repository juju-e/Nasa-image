from flask import Flask, render_template, redirect, send_file,url_for
import requests
import os
import shutil
from forms import enter
import pdfkit
app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
@app.route('/', methods=['GET', 'POST'])
def main():
 global date
 form=enter()
 if form.validate_on_submit():
  res=requests.get("https://api.nasa.gov/planetary/apod?api_key=HN4KWsQZxq6LKTKTh47n6V48A3BrglSYHXO78Un6&date="+str(form.entry.data)).json()
  if 'code' in res:
        return render_template('404.html',msg=res['msg'])
  image_url=res['url']
  date=res['date']
  if os.path.exists(str(date)+'.jpg'):
      os.remove(str(date)+'.jpg')
  if os.path.exists(str(date)+'.pdf'):
      os.remove(str(date)+'.pdf')
  response = requests.get(image_url, stream=True)
  if response.status_code == 200:
    with open(str(date)+".jpg", 'wb') as f:
        f.write(response.content)
  explanation=res['explanation']
  title=res['title']
  preview=render_template('preview.html',url=image_url,expl=explanation,title=title,form=form,date=date)
  preview_file=open(str(date)+'.html','w')
  preview_file.write(preview)
  preview_file.close()
  pdfkit.from_file(str(date)+'.html',str(date)+'.pdf')
  return preview
 return render_template('index.html',form=form)
@app.route('/download/<files>')
def download(files):
   global date
   return send_file(files)
@app.route('/about')
def about():
   return render_template('about.html')

if __name__ == '__main__':
    app.run(port=7080,debug=True)
