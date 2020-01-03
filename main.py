from flask import Flask, render_template, redirect, send_file,url_for # backend stuff
import requests # get the request
import os         # verify if the files exist
import shutil    # write and saving the image
from forms import enter   # form data
import pdfkit         # convert to pdf
app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
@app.route('/', methods=['GET', 'POST'])
def main():
 global date
 form=enter()          # the form's elements
 if form.validate_on_submit():     # if the user submits the form
  res=requests.get("https://api.nasa.gov/planetary/apod?api_key=HN4KWsQZxq6LKTKTh47n6V48A3BrglSYHXO78Un6&date="+str(form.entry.data)).json()
  if 'code' in res:     # if there is an error 
        return render_template('404.html',msg=res['msg'])    # display the 404 page
  image_url=res['url']         # else .... get the url and...
  date=res['date']  # the date
  if os.path.exists(str(date)+'.jpg'):  ######
      os.remove(str(date)+'.jpg')       #  Delete if these files exist
  if os.path.exists(str(date)+'.pdf'):  # 
      os.remove(str(date)+'.pdf')       ######
  response = requests.get(image_url, stream=True)
  if response.status_code == 200:                 #
    with open(str(date)+".jpg", 'wb') as f:       # Download the image and save it with the time index method( as explained in the readme)
        f.write(response.content)                 #
  explanation=res['explanation']            #
  title=res['title']                        # getting other info
  preview=render_template('preview.html',url=image_url,expl=explanation,title=title,form=form,date=date)
  preview_file=open(str(date)+'.html','w')            #
  preview_file.write(preview)                         #  Saving the preview file as a html file
  preview_file.close()                                #
  pdfkit.from_file(str(date)+'.html',str(date)+'.pdf')      # converting to pdf
  return preview
 return render_template('index.html',form=form)
@app.route('/download/<files>')
def download(files):
   global date
   return send_file(files)  # return the file if requested
@app.route('/about')
def about():
   return render_template('about.html')

if __name__ == '__main__':
    app.run(port=7080,debug=True)  # run on port 7080
