import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"

res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
'''
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) #처음으로 발견되는 a엘리먼트를 찾아줌
#print(soup.a.attrs)#속성정보를 출력
#print(soup.a["href"])#특정 속성값 출력


#print(soup.find("a", attrs={"class":"Nbtn_upload"})) #class값이 Nbtn_upload인  a엘리먼트를 찾아라
#print(soup.find(attrs={"class":"Nbtn_upload"}))#class값이 Nbtn_upload인  엘리먼트를 찾아라


#print(soup.find("li",attrs={"class":"rank01"}))
#rank1 = soup.find("li",attrs={"class":"rank01"})
#print(rank1.a.get_text())

rank1 = soup.find("li",attrs={"class":"rank01"})
#print(rank1.a.get_text())
#rank2 = rank1.next_sibling.next_sibling
#rank3 = rank2.next_sibling.next_sibling
#print(rank3.a.get_text())
#rank2 = rank3.previous_sibling.previous_sibling
#print(rank2.a.get_text())

#print(rank1.parent)

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

rank1 = soup.find("li",attrs={"class":"rank01"})
print(rank1.find_next_siblings("li"))

for i in rank1.find_next_siblings("li"):
    print(i.a.get_text())
'''
webtoon = soup.find("a", text="맘마미안-74화")
print(webtoon)
