'''
Developed By Siddhesh Patil
Managed By
Ranjeetsinha Patil and Anupam Patil

Follow me on Instagram for more programs like this https://www.instagram.com/siddhesh1770/
 '''
import time
import datetime
import requests
import pygetwindow as gw

dateTom_base = datetime.date.today() + datetime.timedelta(days=1)
dateTom = dateTom_base.strftime("%d-%m-%Y")
print("Welcome to Seventeen Seventy CO-WIN Vaccine Tracker")
pincode = str(input("Please Enter Your Pincode - "))
findByPinParams = {"pincode": pincode, "date": dateTom}
yikes = []
chromeWindow = gw.getWindowsWithTitle('Co-WIN Application - Google Chrome')[0]
base_urlFindByPin = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
base_urlFindByDistrict = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"


def getrequest(x, y, u):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    r = requests.get(x, y, headers=headers)
    statuscode = r.status_code
    z = r.json()
    if statuscode == 200:
        print("Successfully checked")
    else:
        print("If this happens a lot please restart program or try again after some time.")
    for dictionary in z['sessions']:
        u.append(dictionary['available_capacity'])
    return u


for i in range(5000000):
    getrequest(base_urlFindByPin, findByPinParams, yikes)
    if len(yikes) == 0:
        print("Not Available, Trying again...")
    else:
        chromeWindow.maximize()  # Opens CO-Win Portal if found any slot available
        break
    time.sleep(3)  # Takes pause for 3 seconds,
