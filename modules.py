import urllib2
from bs4 import BeautifulSoup
from twilio.rest import Client

#Fetches an Inspirational Quote from Goodreads and sends as an SMS to your mobile phone


def fetchQuotes():
    url = urllib2.urlopen("https://www.goodreads.com/quotes/tag/inspirational")
    soup = BeautifulSoup(url,'html.parser')
    Quotes=soup.find('div', attrs={'class':'quoteText'})
    fetchedQuote=Quotes.text.strip()
    fetchedQuote=fetchedQuote.split("\n")
    global fetchedQuote_final
    fetchedQuote_final="".join(fetchedQuote)


def sendSms(ToNumber):
    account_sid = "AC515ada73194b79d9ac2cf4aeb340c462"
    token= "ad6ae2a755e90a9f27dd5a17766bf0c8"
    client=Client(account_sid,token)
    client.messages.create(
            to=ToNumber,
            from_="+61481072043",
            body=fetchedQuote_final
        )
    print "Sms sent successfully!"
