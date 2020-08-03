import sys
import pyperclip
import webbrowser
import pyautogui
from bs4 import BeautifulSoup
import re
import csv
from csv import writer
import glob
import os
from datetime import datetime
import time

# pip3 install pyperclip
# pip3 install pyautogui
# pip3 install beautifulsoup4
# pip3 install lxml

filelist=glob.glob("*.html")
for file in filelist:
    os.remove(file)

startrow =801
endrow = 1000


with open('comm_listings_links.csv', 'r') as data_csv:
    data = csv.reader(data_csv)
    for a in range(startrow-1):  # skip the first 500 rows
        next(data)


    rowno = startrow
    count = 0
    # startrow = startrow + 1
    for row in data:

        id = row[0]
        link = row[1]
        title=row[3]
        address= row[4]
        price= row[6]
        psf = row[7]

        webbrowser.open(link)
        time.sleep(12)
        pyautogui.hotkey("command","option","u")
        time.sleep(6)
        pyautogui.hotkey("command","a")
        time.sleep(10)
        pyautogui.hotkey("command","c")
        time.sleep(6)
        data = pyperclip.paste()
        pyautogui.hotkey("command","w")
        pyautogui.hotkey("command","w")

        filename = "tmp.html"


        original = sys.stdout

    # try:

        data = data.replace('png" data-original="', 'png">         <div class="listings_pics">')
        data = data.replace('jpg" class="lazy"', 'jpg</div>')


        print(data)

        with open(filename, 'w') as filehandle:
            # set the new output channel
            sys.stdout = filehandle

            # for line in data:
            print(data)

            # restore the old output channel
            sys.stdout = original

        try:
            for page in glob.glob('*.html'):

                with open(page) as html_file:
                    soup = BeautifulSoup(html_file, 'lxml')

                    print(soup)

                try:
                    dist = soup.find('span', {'itemprop' : 'addressLocality'}).get_text()
                except:
                    dist = ""

                try:
                    category = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[0].get_text()
                except:
                    category = ""

                try:    
                    tenure = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[1].get_text()
                except:
                    tenure = ""

                try:
                    floor_size = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[2].get_text()
                    floor_size = floor_size.replace(' sqft', '')
                except:
                    floor_size = 0


                try:
                    developer = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[3].get_text()
                except:
                    developer = ""

                try:
                    land_size = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[4].get_text()
                    land_size = land_size.replace(' sqft', '')
                except:
                    land_size = ""

                try:
                    furnish = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[6].get_text()
                except:
                    furnish = ""

                try:
                    yearbuilt = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[7].get_text()
                except:
                    yearbuilt = ""

                try:
                    floor_level = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[8].get_text()
                except:
                    floor_level = ""

                try:
                    listingid = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[9].get_text()
                except:
                    listingid = ""

                try:
                    availability = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[10].get_text()
                except:
                    availability = ""

                try:
                    description = soup.find('div', {'class' : 'listing-details-text', 'itemprop' : 'description' }).get_text().strip()
                except:
                    description = ""


                a = category.index('For')
                ofor = category[a+4:]                    
                category = category[:a-1]


                try:
                    cea_reg = soup.find('div', {'class' : 'agent-license'}).get_text()

                    a = cea_reg.index('R')
                    cea_reg = cea_reg[a:a+8]


                except:
                    cea_reg = ""

                agent_id = "12001"
                status = "Active"
                location = title
                listed_on = "2020-05-24 00:00:00+08"


                with open("comm-listings.csv", 'a') as csv_file:
                    csv_writer = writer(csv_file)

                    csv_writer.writerow([id, link,  ofor, title, address, dist, category, tenure, yearbuilt, floor_size,
                    land_size, price, psf, furnish, availability, description, listed_on,
                    status, cea_reg, agent_id])


                with open("comm-listings_img.csv", 'a') as csv_file:
                    csv_writer = writer(csv_file)

                    listings_pics = soup.find_all(class_="listings_pics")

                    for listings_pic in listings_pics:
                        listings_pic = listings_pic.text
                        # print(listings_pic)
                        csv_writer.writerow([id, listings_pic])

                with open("comm-listings_tag.csv", 'a') as csv_file:
                    csv_writer = writer(csv_file)

                    listings_tags = soup.find_all('div', {'class' : 'badge' })

                    for listings_tag in listings_tags:
                        listings_tag = listings_tag.text
                        # print(listings_tag)
                        csv_writer.writerow([id, listings_tag])

                print(title)
                print(id)
                print("Row No " + str(rowno))
                print("")
                print("")

        except:
            error = "Something went wrong"
            with open("listings.csv", 'a') as csv_file:
                csv_writer = writer(csv_file)

                csv_writer.writerow([id, error])

        finally:
            if count > (endrow - startrow -1):
                break

            count +=1
            rowno +=1
