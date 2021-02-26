# Moonbeam_tools
_This is repo with my favorite tools to solving problems using computation, 
algorithms and a variety of technologies._

### JpgToPngConverter 
This is simple python script for converting jpg pictures to png
Script was tested with: python 3.9.1, pillow 8.1.0

All you need copy script in a folder what contain a source picture folder and converted picture folder, run script in terminal

`py jpg_to_png_convector.py from_folder_name into_folder_name`
`from_folder_name` - first parameter
`into_folder_name` - second parameter

if you not created into_folder, just type name like second parameter and python will create for you!

### PdfWaterMarker 
This is script that take one pdf file as an input, another pdf file as a watermark
and create third one, with all pages watermarked 

### Email sender 
This is script can send the email text, or html in email

### Password checker 
The script that help you to check security of your password, 
and check how many times' your password was hacked 

In script used SHA1 hashing and api.pwnedpasswords.com api to check your pass***
by sending only first 5 digits of your hash pass

### SendTextMessages
In this example I used Twilio Cloud Communications api. Using `twilio.rest` api this script can send messages in watsapp or phone text messages

### TwitterBot
Ability to retweet, tweet, follow, search and do a lot more using twitter official api and tweepy library 

### HackerNewsScraper
Can scrap hacker news pages and get the posts with title and links that has specific quantity of votes, 
for example more than 500 or any other number. Project used requests and BeautifulSoup library