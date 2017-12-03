import urllib2
from bs4 import BeautifulSoup
from modules import *
fetchQuotes()
UserPhone=raw_input("Enter The Phone Number you want to send an sms to : ")
sendSms(UserPhone)