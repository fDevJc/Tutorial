import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list.nhn?titleId=602910&weekday=mon"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

windbreakers = soup.find_all("td",attrs={"class":"title"})

for wind in windbreakers :
    title = wind.find("a").get_text()
    link = wind.find("a")["href"]
    star = wind.find_next_sibling("td").find("strong").get_text()
    print(star)
    
#beautifulsoup 도큐먼트있음
