
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

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
print("스크롤 완료")

#스크린샷
browser.get_screenshot_as_file("google_movie.png")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source,"lxml")

#movies = soup.find_all("div",attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]}) #클래스명이 ImZGtf mpg5gc 이거나 Vpfmgd 이거 둘다 가져옴
movies = soup.find_all("div",attrs={"class":"Vpfmgd"}) #클래스명이 ImZGtf mpg5gc 이거나 Vpfmgd 이거 둘다 가져옴

print(len(movies))

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()

    #할인된영화 가지고오기
    sale_movie = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    nosale_movie = movie.find("span",attrs={"class":"VfPpfd ZdBevf"})

    if sale_movie :
        print("영화제목 : {} ,가격 {} -> {}".format(title,sale_movie.get_text(),nosale_movie.get_text()))
    else :
        print("영화제목 : {} ,가격 {}".format(title,nosale_movie.get_text()))
    
