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

with open("condoLinks.csv", 'a') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['id', 'link', 'project']
    csv_writer.writerow(headers)


    id = 1

    for num in range(1,88):
        url = 'https://www.propertyguru.com.sg/condo-directory/search-apartment-project/' + str(num)

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

        a = data.index('col-xs-12 col-sm-7 listing-description')
        data = data[a:]
        # data = str(data)
        data = data.replace('<a class="nav-link" href="', '<div class="A">')
        data = data.replace('" title="', '</div>')
        data = data.replace('itemprop="url">', '<div class="B">')
        data = data.replace('</a></h3>', '</div>')
        data = data.replace('<span itemprop="streetAddress">', '<div class="address">')
        data = data.replace(', singapore ', '</div>   Singapore  <div class="postal">')
        data = data.replace('</span></p>', '</div>')


        with open(filename, 'w') as filehandle:
            # set the new output channel
            sys.stdout = filehandle

            # for line in data:
            print(data)

            # restore the old output channel
            sys.stdout = original
            # print(url)

            soup = BeautifulSoup(data, 'lxml')
        #
            posts=soup.find_all(class_="header-container")

            # count = 1
            for post in posts:
                link = post.find(class_="A").get_text()
                link = "https://www.propertyguru.com.sg" + link

                project = post.find(class_="B").get_text()
                address = post.find(class_="address").get_text()
                postal = post.find(class_="postal").get_text()

                #
                csv_writer.writerow([str(id) ,link, project, address, postal])

                #
                id +=1

                print("")
                print("")
                print(project)
                print(id)
