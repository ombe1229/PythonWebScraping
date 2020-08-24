import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.cgv.co.kr/movies/")
con = req.content

html = BeautifulSoup(con,"html.parser")

ol = html.find("ol")
li = ol.find_all("li")

titlelist = []
scorelist = []

for l in li:
    div = l.find("div",{"class":"box-contents"})
    strong = div.find("strong").text
    titlelist.append(strong)

for l in li:
    div = l.find("div",{"class":"score"})
    strong = div.find("strong").text
    scorelist.append(strong)

for i in range(len(titlelist)):
    print("{}\t".format(i+1)+titlelist[i]+"\t"+scorelist[i])