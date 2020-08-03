import sys
import pyperclip
import webbrowser
import pyautogui
from bs4 import BeautifulSoup
import re
from csv import writer
import glob
import os
from datetime import datetime
import time

filelist=glob.glob("*.html")
for file in filelist:
    os.remove(file)

rowid=700483


for num in range(1,27):
    url = 'https://www.propertyguru.com.sg/property-for-rent/' + str(num) + '?property_type=L'

    webbrowser.open(url)
    time.sleep(5)
    pyautogui.hotkey("command","option","u")
    time.sleep(8)
    pyautogui.hotkey("command","a")
    time.sleep(5)
    pyautogui.hotkey("command","c")
    time.sleep(10)
    data = pyperclip.paste()
    pyautogui.hotkey("command","w")
    pyautogui.hotkey("command","w")

    filename = "tmp.html"


    original = sys.stdout

    try:
        data = data.replace('S$&nbsp;', '<div class="psf">')
        data = data.replace('&nbsp;psf', '</div>')
    except:
        pass

    with open(filename, 'w') as filehandle:
        # set the new output channel
        sys.stdout = filehandle

        # for line in data:
        print(data)

        # restore the old output channel
        sys.stdout = original
        # print(url)


    # parse data
        for page in glob.glob('*.html'):

            with open(page) as html_file:
                soup = BeautifulSoup(html_file, 'lxml')


                listings_links = soup.find_all(class_="listing-description")

                no = 0
                for listing_link in listings_links:
                    link = listing_link.find('a', {'class':'nav-link'})['href']
                    ofor = listing_link.find('a', {'class':'nav-link'})['title']

                    try:
                        title = listing_link.find('a', {'class':'nav-link', 'itemprop':'url'}).get_text()
                    except:
                        title = ""


                    try:
                        address= listing_link.find('span', {'itemprop':'streetAddress'}).get_text()
                    except:
                        address=""

                    try:
                        price= listing_link.find('span', {'class':'price'}).get_text()
                        price= price.replace(',','')
                    except:
                        price =""

                    try:
                        availability= listing_link.find('li', {'class':'listing-availability'}).get_text()
                    except:
                        availability=""

                    try:
                        bed= listing_link.find('span', {'class':'bed'}).get_text()
                    except:
                        bed = ""
                    
                    try:
                        bath= listing_link.find('span', {'class':'bath'}).get_text()
                    except:
                        bath=""
                    
                    try:
                        floor_area= listing_link.find('li', {'class':'listing-floorarea'}).get_text()
                        floor_area= floor_area.replace(' sqft', '')
                    except:
                        floor_area=""
                    
                    try:
                        psf= listing_link.find('div', {'class':'psf'}).get_text()
                    except:
                        psf = ""
                    
                    try:                   
                        listed_on = listing_link.find('div', {'class':'listing-recency'}).get_text()
                    except:
                        listed_on = ""

                    print(rowid)
                    print(title)
                    print("")
                    print("")


                    with open("landed_listings_links.csv", 'a') as csv_file:
                        csv_writer = writer(csv_file)
                        csv_writer.writerow([str(rowid), link, ofor, title, address, floor_area, price, psf, bed, bath, availability, listed_on])


                    no += 1
                    rowid +=1



