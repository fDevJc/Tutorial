#셀레니움 임포트
from selenium import webdriver
import csv
from bs4 import BeautifulSoup

filename = "시가총액1000억이하종목.csv"

f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

#옵션설정
options = webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

#browser 설정
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page=17"

browser.get(url)

#각 옵션 클릭 이벤트 실행
browser.find_element_by_id("option21").click()
browser.find_element_by_id("option6").click()
browser.find_element_by_id("option12").click()
browser.find_element_by_id("option11").click()
browser.find_element_by_id("option25").click()

browser.find_element_by_xpath('//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]/img').click()

browser.get_screenshot_as_file("naver_stock.png")

for page in range(17,31):
    browser.get("https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page="+str(page))
    soup = BeautifulSoup(browser.page_source,"lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]
        if data[8] == "N/A" or data[9] == "N/A":
            continue
        if float(data[8].replace(',','')) <0 :
            print(data[1]," 종목은 매출액증가율 마이너스",data[7])
            continue
        if float(data[9].replace(',','')) <0 :
            print(data[1]," 종목은 영업이익증가율 마이너스",data[8])
            continue
        writer.writerow(data)

f.close()
browser.quit()
