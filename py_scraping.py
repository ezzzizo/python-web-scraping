import json
from bs4 import BeautifulSoup   # importing BS4 libirary
import requests                 # importing request libirary used to get data from links
import re
import csv
import boto3
from csv import writer
import os

#_________________________________
file_name = "data.csv"
#brand = input("please enter the brand you are looking for.")      # with user input
#brand = "alba"
brand = os.getenv("BRAND", "casio")
page = 1
x=0
for page in range(1 , 10):
    
    # Important Note!  
    # Some websites do not allow scraping. To respect this policy, the website name has been replaced with ****.
    
    url = f"https://www.******.com.***/watches-sunglasses/{brand}/?page={page}" # storing link in place called url
    # Fetch data from the URL
    result = requests.get(url) # requesting data from the link
    doc = BeautifulSoup(result.text, "html.parser") # storing url data in place called doc, and converting it into text


    # Extract prices
    item = "EGP"
    price_list = []
    for item in doc.find_all("div", class_= "prc"): # looping on all elements to get all prices
        if not "EGP" in item.text:continue    # checking if the text contains "EGP", if not, skip
        price_list.append(item.string.replace("EGP", ""))  # making a list with all prices
    sample = ","
    j = 0
    for sample in price_list:
        price_list[j] = price_list[j].replace(",", "")
        j = j+1
    for i in range(len(price_list)):  # looping over every price and convert it from string into intger
        price_list[i] = int(float(price_list[i]))


    # Extract product name
    name_list = []
    for item in doc.find_all("h3", class_="name"):
        name_list.append(item.string)
    

    page+1

print("list of product prices:")
print(price_list)
print("=" * 70)    
print("list of product names:")
print(name_list)

#with open('/tmp/' + file_name, "w", encoding="utf-8", newline='') as f:
list =0
with open(file_name, "w", encoding="utf-8", newline='') as f:
    thewriter = csv.writer(f)
    header = ['product_price', 'product_name']
    thewriter.writerow(header)
    o=0
    p=0
    for list in range(len(price_list)):
        thewriter.writerow([price_list[list] , name_list[list]])
        list+1