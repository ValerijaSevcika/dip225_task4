import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook 

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

name=[]
# program read information from people.csv file and put all data in name list. 
with open("people.csv", "r") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(",") 
        name.append(row)

for row in name:
    name_surn = row[2] + " " + row[3]

url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.ID, "input")
find.send_keys("fake")
find = driver.find_element(By.ID, "output")
temp = find.get_attribute("placeholder")
print(temp)
#input_logs.clear()
#input_logs.sent_key(vards-uzvards)