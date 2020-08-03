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

filelist=glob.glob("*.html")
for file in filelist:
    os.remove(file)

id = 17970   #LAST ROW

for num in range(201,340):
    url = 'https://www.propertyguru.com.sg/property-agent-directory/search/' + str(num) + '?limit=30&sort=firstname&order=asc'
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
        a= data.index('<div class="agent-list">')

        b = data.index('<div class="featured-agents-horizontal">')

        data = data[a:b]


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

                    print(soup)

                    agent_cards = soup.find_all('div', {'class' : 'agent-card'})


                    for card in agent_cards:

                        link= card.find('div', {'class': 'agent-photo'}).find('a', href=True).get('href')
                        a = link.index("agent-search") +12
                        link = link[:a]
                        link="https://www.propertyguru.com.sg" + link

                        profile_pic = card.find('div', {'class' : 'agent-photo'}).find('img').get('data-original')
                        agent_name = card.find('div', {'class' : 'agent-info-name'}).get_text().strip()
                        agent_designation = card.find('div', {'class' : 'agent-info-description'}).get_text().strip()

                        active_listings = card.find('div', {'class' : 'agent-info-listing'}).get_text().strip()

                        active_listings = active_listings.replace("No", "")

                        id += 1

                        email = str(id) + "@gmail.com"
                        phone = "9XXXXXXX"
                        active_listings = active_listings.replace(' Active Listings', '')
                        agent_cea = "RXXXXXXC"
                        join_date = datetime.now()
                        verified = "false"
                        verified_date = datetime.now()
                        status = "active"
                        agency_reg = "LXXXXXXX"
                        agency_id = "333333"
                        user_id = id

                        with open("agent_list.csv", 'a') as csv_file:
                            csv_writer = writer(csv_file)


                            csv_writer.writerow([str(id), email, agent_name, phone, active_listings,
                            agent_cea, agent_designation, profile_pic, join_date, verified, verified_date,
                            status, link, agency_reg, agency_id, user_id])

                        print(agent_name)
                        print(link)
                        print(id)
                        print("page no: " + str(num))
                        print(" ")
                        print(" ")

    except:
        print("Something is missing")
