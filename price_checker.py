import requests
from bs4 import BeautifulSoup #This parses and pull individual data from the web site
import smtplib #mail protocol we use to send email
import time #we can use time intervals as we need to set the script to run for a specific time

URL ='https://www.amazon.co.uk/Nespresso-EN550-BM-Lattissima-Automatic-Machine/dp/B013GGO0IC/ref=sr_1_2?crid=2E04R49RNO3GD&keywords=latissima+touch&qid=1578377297&sprefix=lati%2Caps%2C195&sr=8-2' #Set the target item URL that we want to scrape
header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'} #Set the User Agent data. This is data about the device and software that the visitor (my machine) is using
    #Code above returns all the data from the web site that we need to scrape
time_interval_to_check_for_price_drop = 86400

def check_price():
    page = requests.get(URL, headers=header) #Makes a call to the website
    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify()) - Check if our scraper is wokring and we are able to pull data from the website

    #title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:4]) #convert the string of the price to float in order to compare it to our target
    desired_price = 126.00

    if (converted_price < desired_price): 
        notify()
    
def notify():
    server = smtplib.SMTP('smtp.gmail.com', 587) #establish our own email server
    server.ehlo() #establishing connection between two email servers
    server.starttls() #encrypts our connection
    server.ehlo()

    server.login('svetliomu@gmail.com', 'ppglmsyqnoepnzds') #log in to te account wiht the 2-step-authentication

    subject = 'Price for the coffee machine is down'
    body = 'Check the Amazon link ==> https://www.amazon.co.uk/Nespresso-EN550-BM-Lattissima-Automatic-Machine/dp/B013GGO0IC/ref=sr_1_2?crid=2E04R49RNO3GD&keywords=latissima+touch&qid=1578377297&sprefix=lati%2Caps%2C195&sr=8-2'
    msg = f"Subject: {subject}\n\n{body}" #setup the message

    server.sendmail(
        'svetliomu@gmail.com',
        'svetoslav.vl.iliev@gmail.com',
        msg
    )

    print('Email has been sent!')

    server.quit()

while(True): check_price()
time.sleep(time_interval_to_check_for_price_drop)