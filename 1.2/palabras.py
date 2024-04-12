from urllib import request
from urllib.error import URLError

list = ["gilipollas","pendejo","puta"]

def palabrasmalas(url):

    try:
        f = request.urlopen(url)
    except URLError:
        return("La url" +url+ "no existe")
    else:
        aux = f.read()
        contenido = aux.split()
        palabras_encontradas = []
        for l in list:
            for con in contenido:
                if l in con.decode():
                    palabras_encontradas.append(1)
        return palabras_encontradas


url = 'https://es.wikipedia.org/wiki/Lenguaje_soez#Insulto'
print("\n--------------------------------\n")
print("\nInforme de sitio:")
print(palabrasmalas(url))
