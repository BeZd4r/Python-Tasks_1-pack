# He played in fighter club?
from bs4 import BeautifulSoup as BS
import requests
url ="https://ru.kinorium.com/119492/cast/"
r = requests.get(url)

finder = BS(r.text, "html5lib")

while True:
    name = input()
    if finder.find("span", string=f" {name} ") == None:
        print("Персонажа не было в бойцовском клубе")
        print(finder.find("span", string=name))
    else:
        print(f"{name} есть в бойцовском клубе")
