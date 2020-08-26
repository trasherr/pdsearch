{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Search Prodect hi\n",
      "https://www.amazon.in/s?k=hi&ref=nb_sb_noss_2\n",
      "https://www.flipkart.com/search?q=hi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off\n",
      "https://www.reliancedigital.in/search?q=hi:relevance\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "search=input(' Search Prodect ');\n",
    "\n",
    "amazon_url='https://www.amazon.in/s?k='+search+'&ref=nb_sb_noss_2'\n",
    "flipkart_url='https://www.flipkart.com/search?q='+search+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'\n",
    "reliance_url='https://www.reliancedigital.in/search?q='+search+':relevance'\n",
    "\n",
    "header={\"User_Agent\":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}\n",
    "\n",
    "amazon_page=requests.get(amazon_url,headers=header)\n",
    "flipkart_page=requests.get(flipkart_url,headers=header)\n",
    "reliance_page=requests.get(reliance_url,headers=header)\n",
    "\n",
    "amazon_code=BeautifulSoup(amazon_page.content,'html.parser')\n",
    "flipkart_code=BeautifulSoup(flipkart_page.content,'html.parser')\n",
    "reliance_code=BeautifulSoup(reliance_page.content,'html.parser')\n",
    "\n",
    "\n",
    "print(amazon_url)\n",
    "#print(amazon_code)\n",
    "print(flipkart_url)\n",
    "#print(flipkart_code)\n",
    "print(reliance_url)\n",
    "#print(reliance_code)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
