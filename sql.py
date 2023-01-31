#В этом файле я паресрю координаты в sqlite базу
import sqlite3
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect("pogoda")
cur = conn.cursor()

def addInBaze(ind,name,lat,lon):
    cur.execute(f"INSERT INTO cities (nom, name, lat,lon) VALUES ({l}, {name}, {cord[0]},{cord[1]});")
"""def select_name(name):
    cur.execute(f"SELECT name FROM cities WHERE name = {name}")
    result = cur.fetchall()
    return result"""
src = BeautifulSoup(requests.get("https://time-in.ru/coordinates").text)
countries= src.find("ul",class_="coordinates-list").find_all("li")
id = 0
for country in countries:
    urlc = country.find("a").get("href")
    url = BeautifulSoup(requests.get(f"{urlc}").text)
    try:
        cities = url.find("ul",class_="coordinates-items").find_all("li")
        for city in cities:
            id+=1
            name = city.find("a",class_="coordinates-items-left").text
            cord = city.find("div",class_="coordinates-items-right").text.split(",")
            #addInBaze(l,name,float(cord[0]),float(cord[1]))
            params = (id,name,cord[0],cord[1])
            cur.execute(f"INSERT INTO cities VALUES (?, ?, ?,?)",params)
            conn.commit()
    except:
        pass
