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

rowid=0


for num in range(31,32):
    url = 'https://www.propertyguru.com.sg/property-for-sale/' + str(num) + '?property_type=H'

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

        data = data.replace('<h3 class="ellipsis" itemprop="name"><a class="nav-link" href="', '           <div class="listings_links">')
        data = data.replace('" title="For Sale -', '</div>             ')

    except:
        print("Something went wrong")    # data= data.replace('"><img src', '</div>')
        # define content
        # print(a)
        # filecontent = ["Hello, world", "a second line", "and a third line"]

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


                listings_links = soup.find_all(class_="listings_links")

                no = 0
                for listings_link in listings_links:
                    listings_link = listings_link.text
                    print(listings_link)

                    no += 1
                    rowid +=1

                    with open("links.csv", 'a') as csv_file:
                        csv_writer = writer(csv_file)


                        csv_writer.writerow([str(rowid), listings_link])

                        print(str(rowid))
