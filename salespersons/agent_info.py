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



# with open("profile.csv", 'a') as csv_file:
#     csv_writer = writer(csv_file)
    # headers = ['id', 'linkk', 'name', 'designation', 'cea_reg', 'agency_reg', 'phone_no']
    # csv_writer.writerow(headers)

startrow =  1
endrow = 98

with open('profile_notdone1.csv', 'r') as data_csv:
    data = csv.reader(data_csv)
    for a in range(startrow):  # skip the first 500 rows
        next(data)

    count = 0
    # id= startrow + 1
    for row in data:
        url = row[1]
        id = row[0]

        webbrowser.open(url)
        time.sleep(12)
        pyautogui.hotkey("command","option","u")
        time.sleep(5)
        pyautogui.hotkey("command","a")
        time.sleep(8)
        pyautogui.hotkey("command","c")
        time.sleep(8)
        data = pyperclip.paste()
        pyautogui.hotkey("command","w")
        pyautogui.hotkey("command","w")

        filename = "tmp.html"


        original = sys.stdout

        try:
            a = data.index('<div class="container agent-details">')
            b = data.index('<div class="agent-details-top hidden-xs clearfix">')
            data = data[a:b]
            data = data.replace('https:', '           "><div class = "A">https:')
            data = data.replace('.jpg', '.jpg</div>          ')

            data = data.replace('<h3>', '<div class = "B">')
            data = data.replace('<div class="agent-job-title">', '<div class = "C">')
            data = data.replace('</h3>', '</div>')
            data = data.replace('<div class="agent-agency">', '<div class = "D">')
            data = data.replace('licenseNumber=', '           "><div class = "E">')
            data = data.replace('registrationNumber=', '           "><div class = "F">')
            data = data.replace('" target="_blank"', '</div>')
            data = data.replace('</a>', '</div>             ')
            data = data.replace('tel:', '      "> <div class = "G">')
            data = data.replace('" class="agent-btn js-agent-call">', '</div>              ')

            print(data)

            with open(filename, 'w') as filehandle:
                # set the new output channel
                sys.stdout = filehandle

                # for line in data:
                print(data)

                # restore the old output channel
                sys.stdout = original

            for page in glob.glob('*.html'):

                with open(page) as html_file:
                    soup = BeautifulSoup(html_file, 'lxml')
                    profile_pic = soup.find(class_='A').get_text()
                    name = soup.find(class_='B').get_text()
                    designation = soup.find(class_='C').get_text()
                    agency = soup.find(class_='D').get_text()
                    agency_reg= soup.find(class_='E').get_text()
                    agent_cea = soup.find(class_='F').get_text()
                    phone = soup.find(class_='G').get_text()
                    phone = phone[3:]

                    with open("profile.csv", 'a') as csv_file:
                        csv_writer = writer(csv_file)

                        csv_writer.writerow([id, name, designation, agency, agency_reg, agent_cea, phone, profile_pic,url])

                    print(id)
                    print(name)
                    print(designation)
                    print(agency)
                    print(agency_reg)
                    print(agent_cea)
                    print(phone)
                    print(profile_pic)
                    print(url)
                    print("")
                    Print("")

        except:
            error = "Something went wrong"

        finally:
            print(count)

            # if count == 200:
            #     print("sleep now")
            #     time.sleep(3600)
            # elif count == 400:
            #     time.sleep(3600)
            # elif count == 600:
            #     time.sleep(3600)
            # elif count == 800:
            #     time.sleep(3600)

            if count > (endrow - startrow -1):
                break
            count +=1
            # id +=1
