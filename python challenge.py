from prettytable import PrettyTable
from imdb import IMDb

ia = IMDb()

pretty = PrettyTable()

lista = ["Minari","Matrix", "Sound of Metal", "Mank", "Promising Young Woman", "The Father", "Judas and the Black Messiah","The Trial of the Chicago 7","Nomadland"]

pretty.field_names = ["Tittle", "Year","Rating","Director (s)","Plot","Cast (top 5)","Genre"]


for mo in lista:
    directores = ""
    actores = ""
    c = []
    d = []
    result = ia.search_movie(mo)
    result = result[0].movieID
    movie = ia.get_movie(result)
    tittle = mo
    year =movie["year"]
    plot = movie["plot"]
    rating = movie["rating"]
    director = movie["director"][0:5]
    for dir in director:
        d.append(dir["name"])
    directores = ", ".join(d)
    
    cast = movie["cast"][0:5]
    for cas in cast:
        c.append(cas["name"])
    actores= ", ".join(c)
    
    genre = movie["genre"]

    
    pretty.add_row([tittle,year,rating,directores,plot[0],actores,genre[0]])
x = pretty.get_string()
with open('output.txt','w') as archivo_n:
    archivo_n.writelines(x)