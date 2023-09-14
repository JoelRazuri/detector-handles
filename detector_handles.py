"""
  Enunciado: Crea una función que sea capaz de detectar y retornar todos los handles de un texto 
  usando solamente Expresiones Regulares.
  Debes crear una expresión regular para cada caso:
  - Handle usuario: Los que comienzan por "@"
  - Handle hashtag: Los que comienzan por "#"
  - Handle web: Los que comienzan por "www.", "http://", "https://"  y finalizan con un dominio 
    (.com, .es...)  
"""
import re

def dectector_handles(text: str) -> str:
    handles_user = []
    handles_hashtag = []
    handles_web = []

    list_words = text.split(" ")

    for word in list_words:
        if re.findall("^@", word):
            handles_user.append(word)

        if re.findall("^#", word):
            handles_hashtag.append(word)

        if ((re.findall("^www.", word) or re.findall("^http://", word) or re.findall("^https://", word)) and (re.findall(".com$", word) or re.findall(".es$", word))):
            handles_web.append(word)
    
    return handles_user, handles_hashtag, handles_web




def main():
    list_handles = dectector_handles("@Jrazuri Hola #CasiChocamos www.nada www.argentina.com @Abisol helados.es http://helados.es")

    print(f"Handles usuario: {list_handles[0]}\nHandles hashtag: {list_handles[1]}\nHandles web: {list_handles[2]}")


main()