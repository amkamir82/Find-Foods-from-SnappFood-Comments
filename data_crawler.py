import requests
import re
import json

response = requests.get("https://snappfood.ir/search/api/v1/desktop/vendors-list?lat=35.749&long=51.536&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=424837d3-90e3-4c30-b0be-2ea9a482461a&page=0&page_size=20&filters=%7B%22superType%22:[1]%7D&category=%7B%22value%22:1,%22sub%22:[]%7D&query=&sp_alias=restaurant&city_name=Tehran&superType=[1]&extra-filter=&section=SERVICES&vendor_title=&locale=fa")
data = json.loads(response.text)
print(data)

x = data["data"]["result"]
vendor_codes = set()
for i in x:
    y = i["data"]
    if "restaurants" in y:
        for j in y["restaurants"]:
            vendor_codes.add(j["vendorCode"])

print(len(vendor_codes))

my_yrl = "https://snappfood.ir/mobile/v1/restaurant/vendor-comment?client=WEBSITE&vendorCode="
my_url_2 = "&page="
my_url3 = "&sortType=score&locale=fa"

urls = []
num = 1
for i in vendor_codes:
    new_str = my_yrl + str(i) + my_url_2 + str(num) + my_url3
    urls.append(new_str)
    num += 1
    if num == 5:
        break

for j in urls:
    response = requests.get(j)
    data = json.loads(response.text)
    x = data["data"]["comments"]
    for i in x:
        print(i["commentText"])

        print()
        for f in i["replies"]:
            print(f["commentText"])
        print()


response = requests.get("https://snappfood.ir/search/api/v1/desktop/vendors-list?lat=35.73&long=51.431&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=424837d3-90e3-4c30-b0be-2ea9a482461a&page=0&page_size=20&filters=%7B%22superType%22:[1]%7D&category=%7B%22value%22:1,%22sub%22:[]%7D&query=&sp_alias=restaurant&city_name=Tehran&superType=[1]&extra-filter=&section=SERVICES&vendor_title=&locale=fa")

data = json.loads(response.text)

x = data["data"]["finalResult"]
vendor_codes = set()
for i in x:
    y = i["data"]
    vendor_codes.add(y["code"])

my_yrl = "https://snappfood.ir/mobile/v1/restaurant/vendor-comment?client=WEBSITE&vendorCode="
my_url_2 = "&page="
my_url3 = "&sortType=score&locale=fa"

urls = []
num = 21
for i in vendor_codes:
    new_str = my_yrl + str(i) + my_url_2 + str(num) + my_url3
    urls.append(new_str)
    num += 1
    if num == 25:
        break

for j in urls:
    response = requests.get(j)
    data = json.loads(response.text)
    x = data["data"]["comments"]
    for i in x:
        print(i["commentText"])

        print()
        for f in i["replies"]:
            print(f["commentText"])
        print()


response = requests.get("https://snappfood.ir/search/api/v1/desktop/vendors-list?lat=35.7&long=51.353&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=424837d3-90e3-4c30-b0be-2ea9a482461a&page=0&page_size=20&filters=%7B%22superType%22:[1]%7D&category=%7B%22value%22:1,%22sub%22:[]%7D&query=&sp_alias=restaurant&city_name=Tehran&superType=[1]&extra-filter=&section=SERVICES&vendor_title=&locale=fa")

data = json.loads(response.text)

x = data["data"]["finalResult"]
vendor_codes = set()
for i in x:
    y = i["data"]
    vendor_codes.add(y["code"])

my_url1 = "https://snappfood.ir/mobile/v2/restaurant/details/dynamic?optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&vendorCode="
my_url2 = "&show_party=1&fetch-static-data=1&locale=fa"
f = open("New.txt", "a", encoding="utf-8")
urls = []
for i in vendor_codes:
    my_str = my_url1 + str(i) + my_url2
    urls.append(my_str)

for i in urls:
    response = requests.get(i)
    data = json.loads(response.text)
    x = data["data"]["menus"]
    for i in x:
        print(i["category"])
        f.write(i["category"])
        f.write("\n")
        for j in i["products"]:
            print(j["title"])
            f.write(j["title"])
            f.write("\n")
        print()

f.close()

response = requests.get("https://snappfood.ir/search/api/v1/desktop/vendors-list?lat=35.73&long=51.431&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=424837d3-90e3-4c30-b0be-2ea9a482461a&page=0&page_size=20&filters=%7B%22superType%22:[1]%7D&category=%7B%22value%22:7,%22sub%22:[]%7D&query=&sp_alias=restaurant&city_name=Tehran&superType=[1]&extra-filter=&section=SERVICES&vendor_title=&locale=fa")

data = json.loads(response.text)

x = data["data"]["finalResult"]
vendor_codes = set()
for i in x:
    y = i["data"]
    vendor_codes.add(y["code"])

my_url1 = "https://snappfood.ir/mobile/v2/restaurant/details/dynamic?optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&vendorCode="
my_url2 = "&show_party=1&fetch-static-data=1&locale=fa"
f = open("New.txt", "a", encoding="utf-8")
urls = []
for i in vendor_codes:
    my_str = my_url1 + str(i) + my_url2
    urls.append(my_str)

for i in urls:
    response = requests.get(i)
    data = json.loads(response.text)
    x = data["data"]["menus"]
    for i in x:
        print(i["category"])
        f.write(i["category"])
        f.write("\n")
        for j in i["products"]:
            print(j["title"])
            f.write(j["title"])
            f.write("\n")
        print()

f.close()
