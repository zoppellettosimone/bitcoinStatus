#IMPORT

import re
import requests
from bs4 import BeautifulSoup
import time

#CODE

#Waiting time between checks, 10 sec
timeSend = 10

link = "https://www.google.com/search?q=bitcoin&rlz=1C1GCEU_itIT991IT991&oq=bitcoin&aqs=chrome..69i57j0i131i433i512l7j0i433i512j0i131i433i512.3025j1j7&sourceid=chrome&ie=UTF-8"
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

while(True):
    #Find and Take the price from .html id/class in the page url
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #I extract the dd (html) which also contains the price
    priceStr = soup.find_all("span", {"class": "pclqee"})
    #I only extract the price
    price = str(priceStr).replace('[<span class="pclqee">', '').replace('</span>]', '')
    print("Prezzo attuale:", price)

    #Aggiungere la parte di aggiunta nel csv + programma per aprire il Csv tramite grafico

    #Wait for x sec
    time.sleep( timeSend )