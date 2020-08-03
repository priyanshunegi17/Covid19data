import requests
from bs4 import BeautifulSoup
temp= "https://www.worldometers.info/coronavirus/country/"
option={1:"india",2:"us",3:"brazil",4:"pakistan",5:"nepal"}
print("1:india\n2:us\n3:brazil\n4:pakistan\n5:nepal")
a=int(input("choose the desired country\n"))
# country=input("enter the name of country\n")
url=temp+option[a]+"/"

r= requests.get(url)
htmlcontent= r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
print("\nHere are the results....")
ind= soup.find_all('div',id="maincounter-wrap")
for i in range(len(ind)):
    tmp=(ind[i].get_text().strip()).split()
    lenn=len(tmp)
    # print(f"{tmp[0:lenn-1]},{tmp[lenn-1]}")
    print(" ".join(tmp))
    
