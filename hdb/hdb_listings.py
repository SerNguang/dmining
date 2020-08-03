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

startrow =1
endrow = 200


with open('links.csv', 'r') as data_csv:
    data = csv.reader(data_csv)
    for a in range(startrow-1):  # skip the first 500 rows
        next(data)


    rowno = startrow
    count = 0
    # startrow = startrow + 1
    for row in data:


        url = row[1]
        id = row[0]
        webbrowser.open(url)
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

            # except:
            #     error = "Something went wrong"
            # filecontent = ["Hello, world", "a second line", "and a third line"]
        try:
            for page in glob.glob('*.html'):

                with open(page) as html_file:
                    soup = BeautifulSoup(html_file, 'lxml')

                    print(soup)

                    otype = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[0].get_text()
                    tenure = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[1].get_text()
                    floor_size = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[2].get_text()
                    floor_size = floor_size.replace(' sqft', '')
                    developer = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[3].get_text()
                    land_size = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[4].get_text()
                    psf = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[5].get_text()
                    psf = psf.replace('S$ ', '')
                    psf = psf.replace(' psf', '')
                    furnish = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[6].get_text()
                    otop = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[7].get_text()
                    floor_level = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[8].get_text()
                    listingid = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[9].get_text()
                    tenanted = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[10].get_text()
                    listed_on = datetime.now()

                    title = soup.find('h1', {'class' : 'h2', 'itemprop' : 'name'}).get_text().strip()
                    price = soup.find('span', {'itemprop' : 'price' }).get_text().strip()
                    price = price.replace(',', '')
                    bed = soup.find('div', {'class' : 'beds' }).get_text().strip()
                    bath = soup.find('div', {'class' : 'baths' }).get_text().strip()
                    description = soup.find('div', {'class' : 'listing-details-text', 'itemprop' : 'description' }).get_text().strip()

                    a = otype.index('HDB')
                    model = otype[:a-1]

                    b = otype.index('For')
                    ofor = otype[b+4:]

                    # try:
                    #     agent_id = soup.find(class_="agent_id").get_text()
                    # except:
                    #     agent_id = ""

                    # try:
                    #     agent_name = soup.find(class_="gallery-form__agent-name").get_text()
                    # except:
                    #     agent_name = ""

                    # try:
                    #     agent_pic = soup.find('div', {'class' : 'agent-photo'}).attrs['style']
                    #     agent_pic = agent_pic.replace("background-image:url('", "")
                    #     agent_pic = agent_pic.replace("');", "")
                    # except:
                    #     agent_pic = ""

                    # try:
                    #     agent_phone = soup.find('span', {'class' : 'agent-phone-number'}).get_text()
                    # except:
                    #     agent_phone= ""

                    try:
                        agent_license = soup.find('div', {'class' : 'agent-license'}).get_text()

                        a = agent_license.index('R')
                        cea_reg = agent_license[a:a+8]
                        # agency_reg = agent_license[a+11:]

                    except:
                        cea_reg = ""
                        # agency_reg = ""

                    # try:
                    #     agency_name = soup.find('div', {'class' : 'agency-name'}).get_text()
                    # except:
                    #     agency_name = ""


                    # print(id, url)
                    # print(title, ofor, model, tenure, floor_size, developer, land_size, psf, furnish, otop, floor_level,
                    # listingid, tenanted, listed_on)

                    # print(agent_name, agent_phone, agent_license, agency_name, agent_id)

                    agent_id = "12001"
                    hdb_id = "5001"
                    status = "Active"
                    town = ""
                    location = title
                    status = "active"
                    tenure = ""
                    yearbuilt= ""

                    with open("listings.csv", 'a') as csv_file:
                        csv_writer = writer(csv_file)

                        csv_writer.writerow([id, url,  ofor, title, location, dist, model, tenure, yearbuilt, sqft,
                            price, psf, bed, bath, floor_level, furnish, tenanted, otop, description, listed_on,
                            status, cea_reg, hdb_id, agent_id])

                    # with open("listings_agent.csv", 'a') as csv_file:
                    #     csv_writer = writer(csv_file)

                    #     csv_writer.writerow([id, agent_name, agent_phone, agency_name, agency_reg, agent_pic])

                    with open("listings_photos.csv", 'a') as csv_file:
                        csv_writer = writer(csv_file)

                        listings_pics = soup.find_all(class_="listings_pics")

                        for listings_pic in listings_pics:
                            listings_pic = listings_pic.text
                            # print(listings_pic)
                            csv_writer.writerow([id, listings_pic])

                    with open("listings_tags.csv", 'a') as csv_file:
                        csv_writer = writer(csv_file)

                        listings_tags = soup.find_all('div', {'class' : 'badge' })

                        for listings_tag in listings_tags:
                            listings_tag = listings_tag.text
                            # print(listings_tag)
                            csv_writer.writerow([id, listings_tag])

                    print(title)
                    print(id)
                    print("Row No " + str(rowno))

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
