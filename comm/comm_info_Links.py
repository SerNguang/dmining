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

with open("commLinks.csv", 'a') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['id', 'link', 'project']
    csv_writer.writerow(headers)


    id = 810001

    for num in range(1,40):
        url = 'https://www.commercialguru.com.sg/commercial-property-directory/search/' + str(num) + '&limit=10?items_per_page=50'

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

        # a = data.index('col-xs-12 col-sm-7 listing-description')
        # data = data[a:]
        # # data = str(data)
        data = data.replace('<div class="font14"><b><a href="', '<div class="link">')
        data = data.replace('" class="bluelink">', '</div>   <div class="project">')
        data = data.replace('" class="bluelink">', '</div>')
        data = data.replace('<div class="top5"><b>Address:</b> ', '<div class="address">')
        data = data.replace('</b></div>', '</div>')
        # data = data.replace('</span></p>', '</div>')


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
            posts=soup.find_all(class_="blisting_info")

            # count = 1
            for post in posts:
                link = post.find(class_="link").get_text()
                link = "https://www.commercialguru.com.sg" + link

                project = post.find(class_="project").get_text()
                address = post.find(class_="address").get_text()
                postal = address[len(address)-6:]
                address = address[:-7]
                #
                csv_writer.writerow([str(id) ,link, project, address, postal])

                #
                id +=1

                print("")
                print("")
                print(project)
                print(id)
