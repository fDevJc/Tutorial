from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()

url = "https://m.thankqcamping.com/main.hbb"

browser.get(url)

elem = browser.find_element_by_xpath('//*[@id="wrap"]/div[3]/ul/li[2]/a')
elem.click()
