from bs4 import *
import requests as rq
import os
r2=rq.get("https://www.gettyimages.in/photos/aamir-khan-actor")
soup2=BeautifulSoup(r2.text,"https://www.gettyimages.in/photos/aamir-khan-actor")
links=[]
x=soup2.select('img[src^="http://images.gettyimages.in/photos"]')
for img in x:
    links.append(img['src'])
os.mkdir('images')    
i=1
for index, img_link in enumerate(links):
    if i<=60:
        img_data=rq.get(img_link).content 
        with open("images/"+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
            
    else:
        f.close()
        break