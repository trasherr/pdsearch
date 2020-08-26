import requests
from bs4 import BeautifulSoup
import sys

search=sys.argv

amazon_url='https://www.amazon.in/s?k='+search+'&ref=nb_sb_noss_2'
flipkart_url='https://www.flipkart.com/search?q='+search+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
reliance_url='https://www.reliancedigital.in/search?q='+search+':relevance'

header={"User_Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

amazon_page=requests.get(amazon_url,headers=header)
flipkart_page=requests.get(flipkart_url,headers=header)
reliance_page=requests.get(reliance_url,headers=header)

amazon_code=BeautifulSoup(amazon_page.content,'html.parser')
flipkart_code=BeautifulSoup(flipkart_page.content,'html.parser')
reliance_code=BeautifulSoup(reliance_page.content,'html.parser')


#print(amazon_url)
#print(amazon_code)
#print(flipkart_url)
#print(flipkart_code)
print(reliance_url)
#print(reliance_code)