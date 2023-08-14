from bs4 import BeautifulSoup
import requests

archivo = open("database.sql","w",encoding="Utf-8")

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

    print("INSERT INTO GRUPO(nombreGrupo,imagenGrupo) VALUES('" + nombreGrupo + "','-');")
    archivo.write("INSERT INTO GRUPO(nombreGrupo,imagenGrupo) VALUES('" + nombreGrupo + "','-');")

    for item2 in canciones:
        if item2 == []:
            continue
        nombreCancion = item2.find("a").get_text()
        if '\'' in nombreCancion:
            nombreCancion.replace('\'', '`')
        print("INSERT INTO CANCION(id_grupo,nombreCancion) VALUES(" + str(box.index(item)) + ",'" + nombreCancion +"');")
        archivo.write("INSERT INTO CANCION(id_grupo,nombreCancion) VALUES(" + str(box.index(item)) + ",'" + nombreCancion +"');")

archivo.close()