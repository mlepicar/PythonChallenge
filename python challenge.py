from prettytable import PrettyTable
from imdb import IMDb

ia = IMDb()

pretty = PrettyTable()

lista = ["Minari", "Sound of Metal", "Mank", "Promising Young Woman", "The Father", "Judas and the Black Messiah","The Trial of the Chicago 7","Nomadland"]

pretty.field_names = ["Year","Rating","Director (s)","Plot","Cast (top 5)","Genre"]


for mo in lista:
    directores = []
    actores = []
    result = ia.search_movie(mo)
    result = result[0].movieID
    movie = ia.get_movie(result)
    year =movie["year"]
    plot = movie["plot"]
    rating = movie["rating"]
    director = movie["director"]
    cast = movie["cast"]
    genre = movie["genre"]
    for d in director:
        director = ia.get_person(d.personID)
        directores.append(director["name"])
    for c in range(0,5):
        person = ia.get_person(cast[c].personID)
        actores.append(person["name"])
    pretty.add_row([year,rating,directores[0],plot[0],actores,genre[0]])
x = pretty.get_string()
with open('output.txt','w') as archivo_n:
    archivo_n.writelines(x)