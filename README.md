# doman-web
Simple web app to teach toddlers numbers
# Background
The book [How to teach your baby math](https://www.amazon.com/How-Teach-Your-Baby-Math-ebook/dp/B00IAQRZ3G/), by Glenn Doman, recommends teaching babies/toddlers numbers by showing them cards with dots on them, whilst saying the number aloud.

Instead of making your own cards and using your own voice, you can run this web app and use your smartphone and thumb.
# Server requirements
* Linux
* Python 3.x
# Client requirements
* A web browser that supports the Web Speech API for speech synthesis (e.g. Chrome for Android)
# How to run the server
1. Clone the repo
```https://github.com/rahimnathwani/doman-web.git```
2. Change into the directory
```cd doman-web```
3. Install flask
```pip install -r requirements.txt```
4. Run the app locally
```
export FLASK_APP=main.py
flask run --host=0.0.0.0
```
# How to use it
1. Browse to http://127.0.0.1/1/20
2. Tap anywhere on the screen. You should see some dots, and hear the number of dots. After ~1 second, the screen will go blank again, and you can tap again to see a new random number.
# More info
* If you don't want to use the range of numbers 1 to 20, then replace the numbers in the URL above
* To use it in your smartphone, just replace the IP address above, with the IP address of your computer
