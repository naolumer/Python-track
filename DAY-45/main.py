import requests
from bs4 import BeautifulSoup

response= requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

sourcetext= response.text

soup= BeautifulSoup(sourcetext, "html.parser")

titles= soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
just_titles=[]

for title in titles:
    txt= title.get_text()
    just_titles.append(txt)

movies=just_titles[::-1]

with open("./DAY-45/movies_list.txt", mode= "w") as file:
    
    for movie in movies:
        file.write(f"{movie}\n")



    


    
    


    