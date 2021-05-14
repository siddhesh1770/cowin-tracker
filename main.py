"""
Developed By Siddhesh Patil
Managed By
Ranjeetsinha Patil and Anupam Patil
Follow me on Instagram for more programs like this https://www.instagram.com/siddhesh1770/
 """
import time
import datetime
import requests
import pygetwindow as gw
list1 = []
list2 = []
list3 = []
dateTom_base = datetime.date.today() + datetime.timedelta(days=1)
dateTom = dateTom_base.strftime("%d-%m-%Y")
print("Welcome to Seventeen Seventy CO-WIN Vaccine Tracker")
pincode = str(input("Please Enter Your Pincode - "))
list3.append(int(input("Enter Age Limit 18 OR 45 - ")))
sec = float(input("Please enter time Interval in seconds (3 is Recommended) But if slot is about to open you can "
                  "also enter 0.5 OR 1 also - "))
findByPinParams = {"pincode": pincode, "date": dateTom}
chromeWindow = gw.getWindowsWithTitle('Co-WIN Application - Google Chrome')[0]
base_urlFindByPin = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
base_urlFindByDistrict = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"

def getrequest(x, y, u, v):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    r = requests.get(x, y, headers=headers)
    statuscode = r.status_code
    z = r.json()
    p = r.json()
    if statuscode == 200:
        print("Successfully checked")
    else:
        print("If this happens a lot please restart program or try again after some time.")
    for dictionary1 in z['sessions']:
        u.append(dictionary1['available_capacity'])
    for dictionary2 in p['sessions']:
        v.append(dictionary2['min_age_limit'])
    return u, v

for i in range(5000000):
    getrequest(base_urlFindByPin, findByPinParams, list1, list2)
    if len(list1) > 0 and list2[0] == list3[0]:
        chromeWindow.maximize()  # Opens CO-Win Portal if found any slot available
        break
    else:
        print("Not available trying again !!!")
        print("Trial Number = "+str(i + 1))
    time.sleep(sec)  # Takes pause for 3 seconds
