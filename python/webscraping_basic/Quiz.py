import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#hrml파일 만들기
#with open("quiz.html","w",encoding="utf8") as f:
#          f.write(soup.prettify())


table = soup.find("table",attrs={"class":"tbl"})
trs = table.find_all("tr")

for idx,tr in enumerate(trs):
    columns = tr.find_all("td")
    if idx == 0:
        continue
    print("="*5,"매물",str(idx),"="*5)
    #print("거래 :",tr.find("td",attrs={"class":"col1"}).get_text())
    print("거래 :",columns[0].get_text())
    #print("면적 :",tr.find("td",attrs={"class":"col2"}).get_text())
    print("면적 :",columns[1].get_text())
    #print("가격 :",tr.find("td",attrs={"class":"col3"}).get_text())
    #print("동 :",tr.find("td",attrs={"class":"col4"}).get_text())
    #print("층 :",tr.find("td",attrs={"class":"col5"}).get_text())
        
