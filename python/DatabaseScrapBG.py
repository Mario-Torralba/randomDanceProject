from bs4 import BeautifulSoup
import requests

archivo = open("database.sql","w",encoding="Utf-8")

website = "https://kpopping.com/profiles/the-groups/men"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, "lxml")


box = soup.find_all("div",class_="item")
cantidad = 0
for item in box:

    nombreGrupo = item.find("a").get_text().replace("'","´")
    enlaceGrupo = item.find("a").get("href")

    websiteFor = "https://kpopping.com" + enlaceGrupo
    resultFor = requests.get(websiteFor)
    contentFor = resultFor.text

    soupFor = BeautifulSoup(contentFor, "lxml")
    canciones = soupFor.find_all("div",class_="title-wr")

    temp = "INSERT INTO GRUPO(id_grupo,nombreGrupo,imagenGrupo) VALUES('A" + str(box.index(item)) + "','" + nombreGrupo + "','-');"

    print(temp)
    archivo.write(temp)

    for item2 in canciones:
        if item2 == []:
            continue
        nombreCancion = item2.find("a").get_text()
        if "'" in nombreCancion:
            nombreCancion2 = nombreCancion.replace("'", "´")
        else:
            nombreCancion2 = nombreCancion

        temp2 = "INSERT INTO CANCION(id_grupo,nombreCancion) VALUES('A" + str(box.index(item)) + "','" + nombreCancion2 +"');"

        print(temp2)
        archivo.write(temp2)

archivo.close()