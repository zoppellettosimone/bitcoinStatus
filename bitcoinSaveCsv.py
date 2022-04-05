#IMPORT

import re
import requests
from bs4 import BeautifulSoup
import time
from datetime import date
from datetime import datetime
import time
import os

#CODE

#Waiting time between checks, 1 hour
timeSend = 3600
timeToExe = 0

link = "https://www.google.com/search?q=bitcoin&rlz=1C1GCEU_itIT991IT991&oq=bitcoin&aqs=chrome..69i57j0i131i433i512l7j0i433i512j0i131i433i512.3025j1j7&sourceid=chrome&ie=UTF-8"
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

while(True):
    #Find and Take the price from .html id/class in the page url
    page = requests.get(link, headers=headers)
    timeToExe = time.time()
    soup = BeautifulSoup(page.content, 'html.parser')

    #I extract the dd (html) which also contains the price
    priceStr = soup.find_all("span", {"class": "pclqee"})
    #I only extract the price
    price = str(priceStr).replace('[<span class="pclqee">', '').replace('</span>]', '').replace('.', '').replace(',', '.')
    print("Prezzo attuale:", price)

    print(date.today().strftime("%Y-%m"))

    # Change the current directory
    cwd = os.getcwd()
    # Check if there is Csv Folder
    listDir = os.listdir()
    #Check Variable
    thereis = False
    #Check if the Folder exist
    for j in range(0, len(listDir), 1):
        if((cwd + '\\' + listDir[j]) == (cwd + "\\Csv")):
            thereis = True
    # mkdir "Csv"
    if(thereis == False):
        os.mkdir(cwd + "\Csv")


    #Scrittura sul File del Mese
    #Apertura File
    file = open(cwd + "\\Csv\\" + date.today().strftime("%Y-%m") + ".csv","w") 

    #Check if file exist or no
    thereis = False
    for j in range(0, len(listDir), 1):
        if((cwd + '\\' + listDir[j]) == (cwd + "\\Csv\\" + date.today().strftime("%Y-%m") + ".csv")):
            thereis = True

    #if file not exist
    if(thereis == False):
        #Add Header Column
        file.write(str("Date,Price"))
 
    #Scrittura su File
    file.write(str("\n" + datetime.now().strftime("%d:%H")) + "," + str(price))
    
    #Fine Scrittura
    file.close()
    
    #Scrittura sul File dell'Anno
    #Apertura File
    file = open(cwd + "\\Csv\\" + date.today().strftime("%Y") + ".csv","w") 

    #Check if file exist or no
    thereis = False
    for j in range(0, len(listDir), 1):
        if((cwd + '\\' + listDir[j]) == (cwd + "\\Csv\\" + date.today().strftime("%Y-%m") + ".csv")):
            thereis = True

    #if file not exist
    if(thereis == False):
        #Add Header Column
        file.write(str("Date,Price"))
 
    #Scrittura su File
    file.write(str("\n" + datetime.now().strftime("%d/%m:%H")) + "," + str(price))
    
    #Fine Scrittura
    file.close()

    print("Wait 1 hour")

    #Wait for x sec
    time.sleep( timeSend - (time.time() - timeToExe) )