#import requests
#from bs4 import BeautifulSoup
'''
url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    ,"Accept-Language":"ko-KR,ko"
    }
res = requests.get(url,headers=headers)

res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})

print(len(movies))

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()

    print(title)

#soup.prettify() html 문서를 이쁘게 만들어줌
'''

from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

#지정한 위치로 스크롤 내리기 높이 1080위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,2080)")

#화면 가장 아래로 스크롤 내리기
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 #2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복수행
while True:
    #스크롤을 가장아래로 
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

    
