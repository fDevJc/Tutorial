from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

#1. 네이버로 이동
browser.get("http://naver.com")

#2. 로그인버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. 아이디입력
elem = browser.find_element_by_id("id")
elem.send_keys("naver_id")
#4. 패스워드입력
elem = browser.find_element_by_id("pw")
elem.send_keys("password")
#5. 로그인버튼 클릭
elem = browser.find_element_by_id("log.login")
elem.click()

#이렇게 할경우 뒤에 붙어서 나옴
#elem = browser.find_element_by_id("id").send_keys("my_id")


browser.find_element_by_id("id").clear()
elem = browser.find_element_by_id("id").send_keys("my_id")

#6. html 정보 출력
print(browser.page_source)

#브라우저 종료
browser.quit()
