from bs4 import BeautifulSoup
import requests

website = "https://kpopping.com/profiles/the-groups/men"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, "lxml")


box = soup.find_all("div",class_="item")

for item in box:

    nombreGrupo = item.find("a").get_text()
    enlaceGrupo = item.find("a").get("href")

    websiteFor = "https://kpopping.com" + enlaceGrupo
    resultFor = requests.get(websiteFor)
    contentFor = resultFor.text

    soupFor = BeautifulSoup(contentFor, "lxml")
    canciones = soupFor.find_all("div",class_="title-wr")

    print(nombreGrupo + " --> https://kpopping.com" + enlaceGrupo + " " + str(box.index(item)))

    for item in canciones:
        if item == []:
            continue
        nombreCancion = item.find("a").get_text()
        print(nombreCancion)

