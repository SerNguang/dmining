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

time_start = datetime.now()


filelist=glob.glob("*.html")
for file in filelist:
    os.remove(file)


startrow = 1
endrow = 10


with open('condoLinks.csv', 'r') as data_csv:
    data = csv.reader(data_csv)
    for a in range(startrow):  # skip the first 500 rows
        next(data)

    count = 0

    for row in data:
        url = row[1]
        id = row[0]
        address = row[3]
        postal = row[4]

        # try:
        webbrowser.open_new(url)
        # webbrowser.open(url)
        time.sleep(12)
        pyautogui.hotkey("command","option","u")
        time.sleep(10)
        pyautogui.hotkey("command","a")
        time.sleep(8)
        pyautogui.hotkey("command","c")
        time.sleep(8)
        data = pyperclip.paste()
        pyautogui.hotkey("command","w")
        pyautogui.hotkey("command","w")

        filename = "tmp.html"


        original = sys.stdout

        with open(filename, 'w') as filehandle:
            # set the new output channel
            sys.stdout = filehandle

        # try:
            data = data.replace('" itemprop="image" content="', '">           <div class="project-pic">')
            data = data.replace('.jpg">', '.jpg</div>')
            data = data.replace('.png">', '.png</div>')

            data = data.replace('<tr><td>Building @ ', '<div class="building">')
            data = data.replace('</td><td', '</div>        <div><td')
            data = data.replace(' itemprop="description"', '')

        # for line in data:</td><td>
            print(data)

            # restore the old output channel
            sys.stdout = original


            soup = BeautifulSoup(data, 'lxml')


# ################################################################################################################
#             street = soup.find('span', {'itemprop': 'streetAddress'}).get_text()
#             dist = street[-4:-1]
#
#             project = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[0].get_text()
#
#             type = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[1].get_text()
#
#             developer = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[2].get_text()
#
#             tenure = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[3].get_text()
#
#             built_year = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[6].get_text()
#
#             floor_nos = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[7].get_text()
#
#             units = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[8].get_text()
#
#             description = soup.find(class_="listing-details-description").get_text()
#             description = description.strip()

####################################################################################################################

            try:
                street = soup.find('span', {'itemprop': 'streetAddress'}).get_text()
                dist = street[-4:-1]
            except:
                dist = ""

            try:
                project = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[0].get_text()
            except:
                project = ""

            try:
                category = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[1].get_text()
            except:
                category = ""

            try:
                developer = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[2].get_text()
            except:
                developer = ""

            try:
                tenure = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[3].get_text()
            except:
                tenure = ""

            try:
                built_year = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[6].get_text()
            except:
                built_year =""

            try:
                storeys = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[7].get_text()
            except:
                storeys = ""

            try:
                project_size = soup.find_all('div', {'class' : 'value-block', 'itemprop' : 'value' })[8].get_text()
            except:
                project_size = ""

            try:
                description = soup.find(class_="listing-details-description").get_text()
                description = description.strip()
            except:
                description = ""

            slug= ""
            title = project

            print("")
            print("")
            print(project)
            print(id)

            with open("condoinfo.csv", 'a') as csv_file:
                csv_writer = writer(csv_file)
                csv_writer.writerow([id, url, category, title, project, address, slug, dist, postal, tenure, built_year, 
                storeys, project_size, developer, description])


            with open("project_pics.csv", 'a') as csv_file:
                csv_writer = writer(csv_file)

                project_pics = soup.find_all(class_="project-pic")

                for pic in project_pics:
                    pic = pic.text
                    csv_writer.writerow([id, pic])

            with open("building.csv", 'a') as csv_file:
                csv_writer = writer(csv_file)

                buildings = soup.find_all(class_="building")

                for building in buildings:
                    building = building.text
                    csv_writer.writerow([id, building])
        # except:
            # print("Something is missing")

#
        # finally:
            if count > (endrow - startrow -1):
                break
            count +=1
    #
#
# time_end = datetime.now()
#
# print(time_start)
# print(time_end)
