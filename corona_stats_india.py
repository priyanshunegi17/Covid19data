import requests
from bs4 import BeautifulSoup

url="https://www.mygov.in/covid-19"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
div=soup.find_all('tr')
a=[]
for i in range(len(div)):
    b=(div[i].get_text())
    a.append(b.split())
# for state in a:
#     for i in state:
#         i.rjust(20,"p")
#     print(" ".join())
f=open("corona1.csv","w")
for key in a:
    k=len(key)
    if "Dadra" in key:
        a=" ".join(key[0:4])
    else:
        a=" ".join(key[:k-4])
    
    print(f"{a.replace(',','').ljust(30,' ')} {key[k-4].replace(',','').ljust(20,' ')} {key[k-3].replace(',','').ljust(20,' ')} {key[k-2].replace(',','').ljust(20,' ')} {key[k-1].replace(',','').ljust(20,' ')}")
    f.write(f"{a.replace(',','').ljust(30,' ')},{key[k-4].replace(',','').ljust(20,' ')},{key[k-3].replace(',','').ljust(20,' ')},{key[k-2].replace(',','').ljust(20,' ')},{key[k-1].replace(',','').ljust(20,' ')}\n")
f.close()    


