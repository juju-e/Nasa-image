# Nasa-image
A flask web app that fetchs nasa's Astronomy Picture of the day and displays it, it has a download as pdf option
This wab app depends on wkhtmltopdf, to install it just type:
```

$ sudo apt install wkhtmltopdf

```
or if you are using a red-hat based distro
```
$ sudo dnf install wkhtmltopdf
```
To install the needed pip packeges be sure to be in the folder in which you installed this web app and run:
```
$ pip install -r requirements.txt
```
To run this app type: ` python3 main.py ` The server will be running on localhost port 7080

#### In this introductory readme, i'm going to explain the steps i took to make this web app.
#### First i registered to [https://api.nasa.gov/](https://api.nasa.gov/) and got a key, this certainly was the easyest part of this task, I immediately started to make a responsive and sympatic frontend for the web app, which also proved to be pretty easy.
#### I Then started working on the backend, This one was a very, very hard thing i did. I faced 2 major issues:
####   - I Struggled for a whole day almost without sleeping to find a way to convert the file to pdf
####   - I also struggled on how the server will know which pdf to download

#### Thanks god i also finally found 2 solutions to the 2 enumerated problems:

### 1.Pdfkit:

#### I used this simple python module to convert the obtained html file(after the user gives the date) into a pdf file,but the problem still lied on how to index them, that's where solution 2 enter's the game
### 2.Index by date:
#### For the server to know which file(image, html, pdf) it was working on, i first though of creating a single name('img') and add .txt .html and .pdf extensions and after the user used the file, they would automatically be deleted.
<br>

#### But this made me loose at least 6 hours of debugging, 'cause OMG this method was so much buggy and sloppy that it almost made me abbandon the task, but later on i found an article on how some websites index their files, that they associate each file with a unix timestamp of when the file was uploaded,
<br>

#### I got back to work and used the same method but in place of using an unique unix timestamp for each file, i simply associated a file(pdf,jpg,html) with the date at which it was uploaded on [api.nasa.gov/](https://api.nasa.gov/) which by the way is unique for every image.
<br>

#### It then became pretty easy to know which html file was to be transformed into a pdf, which jpg i was gonna display and which pdf the user is gonna download.
