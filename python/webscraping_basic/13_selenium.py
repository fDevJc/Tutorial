from selenium import webdriver

#browser = webdriver.Chrome("./chromedriver.exe")

browser = webdriver.Chrome()

browser.get("http://naver.com")

C:\python\webscraping_basic>python
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from selenium import webdriver
>>> browser = webdriver.Chrome()

DevTools listening on ws://127.0.0.1:63026/devtools/browser/c28ab5b2-391d-4ba0-88ed-8f82dcdf692f
>>> [9316:16764:1228/203327.755:ERROR:device_event_log_impl.cc(211)] [20:33:27.756] USB: usb_device_handle_win.cc:1020 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습 니다. (0x1F)
browser = webdriver.Chrome()

DevTools listening on ws://127.0.0.1:63044/devtools/browser/c242e342-f21a-45dd-b5cd-62720444c758
>>> [20072:13772:1228/203358.044:ERROR:device_event_log_impl.cc(211)] [20:33:58.044] USB: usb_device_handle_win.cc:1020 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
^Z
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> browser = webdriver.Chrome()

DevTools listening on ws://127.0.0.1:63062/devtools/browser/ec3c6366-9293-4304-a3b1-05c56f180e2d
>>> "                 28/203433.111:ERROR:device_event_log_impl.cc(211)] [20:34:33.111] USB:
  File "<stdin>", line 1:1020 Failed to read descriptor from node connection: 시스템에 부착된    "가 작동하지 않습니다. (0x1F)
     ^
SyntaxError: EOL while scanning string literal
>>>
>>>
>>>
>>> browser.get("http://naver.com")
>>> elem = browser.find_element_by_class_name("link_login")
>>> elem
<selenium.webdriver.remote.webelement.WebElement (session="8c60d30a5c2380631cb29b3f8e8fb118", element="37450c8b-d8cc-4c38-88c5-0bd889f4aee4")>
>>> elem.click()
>>> browser.back()
>>> browser.forward()
>>> browser.refresh()
>>> browser.bakc()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'WebDriver' object has no attribute 'bakc'
>>> browser.back()
>>> elem = browser.find_element_by_id("query")
>>> elem
<selenium.webdriver.remote.webelement.WebElement (session="8c60d30a5c2380631cb29b3f8e8fb118", element="30eb8b05-e47d-4ad6-a5f9-faac8143250b")>
>>> from selenium.webdriver.common.keys import keys
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'keys' from 'selenium.webdriver.common.keys' (C:\Users\양지철\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\common\keys.py)
>>> from selenium.webdriver.common.keys import Keys
>>> elem.send_keys("나도코딩")
>>> elem.send_keys(Keys.ENTER)
>>> elem = browser.find_element_by_tag_name("a")
>>> elem
<selenium.webdriver.remote.webelement.WebElement (session="8c60d30a5c2380631cb29b3f8e8fb118", element="3376a2ac-cfa5-428d-b6b4-e50a3eed7f9b")>
>>>
>>>
>>>
>>>
>>>
>>>
>>> elem = browser.find_elements_by_tag_name("a")
>>> for e in elem:
...     elem.get_attribute("href")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'list' object has no attribute 'get_attribute'
>>>
>>> for e in elem:
...     e.get_attribute("href")
...
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#lnb'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#content'
'https://www.naver.com/'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://help.naver.com/support/alias/search/word/word_29.naver'
'https://help.naver.com/support/alias/search/word/word_29.naver'
'https://help.naver.com/support/alias/search/word/word_29.naver'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://help.naver.com/support/alias/search/word/word_16.naver'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://help.naver.com/support/alias/search/word/word_16.naver'
'https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fwhere%3Dnexearch%26sm%3Dtop_hty%26fbm%3D0%26ie%3Dutf8%26query%3D%25EB%2582%2598%25EB%258F%2584%25EC%25BD%2594%25EB%2594%25A9'
'https://help.naver.com/support/alias/search/word/word_16.naver'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://help.naver.com/support/alias/search/word/word_17.naver'
'https://help.naver.com/support/alias/search/word/word_18.naver'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fwhere%3Dnexearch%26sm%3Dtop_hty%26fbm%3D0%26ie%3Dutf8%26query%3D%25EB%2582%2598%25EB%258F%2584%25EC%25BD%2594%25EB%2594%25A9'
'javascript:;'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://nid.naver.com/user2/api/naverProfile.nhn?m=checkIdType'
'https://nid.naver.com/user2/api/naverProfile.nhn?m=checkIdType'
'https://nid.naver.com/nidlogin.logout?returl=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fwhere%3Dnexearch%26sm%3Dtop_hty%26fbm%3D0%26ie%3Dutf8%26query%3D%25EB%2582%2598%25EB%258F%2584%25EC%25BD%2594%25EB%2594%25A9'
'https://mail.naver.com/'
'https://nid.naver.com/user2/help/myInfo.nhn?menu=home'
'https://nid.naver.com/user2/help/myInfo.nhn?m=viewSecurity&menu=security'
'https://nid.naver.com/user2/eSign/v1/home/land'
'https://nid.naver.com/membership/my'
'https://pay.naver.com/'
'https://blog.naver.com/MyBlog.nhn'
'https://section.cafe.naver.com/'
'https://pay.naver.com/'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'javascript:;'
'https://noti.naver.com/index.nhn'
'https://mail.naver.com/'
'javascript:;'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://cafe.naver.com/'
'https://news.naver.com/'
'https://map.naver.com/'
'https://sports.news.naver.com/'
'https://game.naver.com/'
'https://section.blog.naver.com/'
'https://post.naver.com/main.nhn'
'https://dict.naver.com/'
'https://kin.naver.com/'
'https://n.weather.naver.com/'
'https://mail.naver.com/'
'https://stock.naver.com/'
'https://land.naver.com/'
'https://vibe.naver.com/today/'
'https://book.naver.com/'
'https://shopping.naver.com/'
'https://comic.naver.com/'
'https://movie.naver.com/'
'https://mybox.naver.com/'
'https://auto.naver.com/'
'https://campaign.naver.com/npay/rediret/index.nhn'
'https://www.naver.com/more.html'
'https://www.naver.com/more.html'
'https://dict.naver.com/'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://book.naver.com/search/search.nhn?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=video&sm=tab_jum&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.shopping.naver.com/search/all.nhn?where=all&frm=NVSCTAB&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=realtime&sm=tab_jum&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://dict.naver.com/search.nhn?dicQuery=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&target=dic&query_utf=&isOnlyViewEE='
'https://map.naver.com/v5/search/%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://vibe.naver.com/search?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=kdic&sm=tab_jum&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://audioclip.naver.com/search/all?keyword=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://academic.naver.com/search.naver?field=0&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://help.naver.com/support/alias/search/integration/integration_4.naver'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://www.youtube.com/channel/UC7iAOLiALt2rtMVAWWl4pnw'
'https://www.youtube.com/channel/UC7iAOLiALt2rtMVAWWl4pnw'
'https://www.youtube.com/channel/UC7iAOLiALt2rtMVAWWl4pnw'
'https://www.youtube.com/channel/UC7iAOLiALt2rtMVAWWl4pnw'
'https://play.google.com/store/apps/details?id=com.hafali.cardpair'
'https://play.google.com/store/apps/details?id=com.hafali.pyramid'
'https://help.naver.com/support/alias/search/contents/contents08.naver'
'https://m.onestore.co.kr/'
'https://www.apple.com/kr/app-store/'
'https://play.google.com/store/apps'
'https://search.naver.com/search.naver?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&nso=&where=view&sm=tab_viw.all&mode=normal'
'https://search.naver.com/search.naver?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&nso=&where=blog&sm=tab_viw.all'
'https://search.naver.com/search.naver?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&nso=&where=article&sm=tab_viw.all'
'https://search.naver.com/search.naver?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&nso=&where=view&sm=tab_viw.all&mode=normal'
'https://search.naver.com/search.naver?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&nso=&where=view&sm=tab_viw.all&mode=timeline'
'https://search.naver.com/search.naver?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&nso=&where=view&sm=tab_viw.all&mode=image'
'https://blog.naver.com/yuzyoe/222184041560'
'https://blog.naver.com/yuzyoe'
'https://blog.naver.com/yuzyoe'
'https://blog.naver.com/yuzyoe/222184041560'
'https://blog.naver.com/yuzyoe/222184041560'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9%EC%A7%80%EB%8F%84%EC%82%AC'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9%EC%A7%80%EB%8F%84%EC%82%AC%EC%9E%90%EA%B2%A9%EC%A6%9D'
'https://blog.naver.com/simon9627/221848111545'
'https://blog.naver.com/simon9627'
'https://blog.naver.com/simon9627'
'https://blog.naver.com/simon9627/221848111545'
'https://blog.naver.com/simon9627/221848111545'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=AI'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%99%9C%EC%9A%A9%ED%95%9C'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%95%B1'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EB%A7%8C%EB%93%A4%EA%B8%B0'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%96%B4%ED%94%8C%ED%95%98%EB%82%98%EB%A9%B4'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9%EB%A7%88%EC%8A%A4%ED%84%B0'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EA%B5%90%EC%9C%A1%EC%95%B1'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%8A%A4%EB%A7%88%ED%8A%B8%EB%A9%94%EC%9D%B4%EC%BB%A4'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%9E%85%EB%AC%B8%EA%B5%90%EC%9C%A1'
'https://blog.naver.com/you_0_0/222186625399'
'https://blog.naver.com/you_0_0'
'https://blog.naver.com/you_0_0'
'https://blog.naver.com/you_0_0/222186625399'
'https://blog.naver.com/you_0_0/222186625399'
'https://blog.naver.com/kos339'
'https://blog.naver.com/kos339'
'https://blog.naver.com/kos339/222188106045'
'https://blog.naver.com/kos339/222188106045'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%8F%85%ED%95%99'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%9C%A0%ED%88%AC%EB%B2%84'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9%EC%84%A0%EC%83%9D%EB%8B%98'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9%EA%B3%B5%EB%B6%80'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EA%B0%9C%EB%B0%9C%EC%9E%90'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EB%AC%B8%EA%B3%BC'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=python3'
'https://blog.naver.com/wjdwngkdsla/221884221493'
'https://blog.naver.com/wjdwngkdsla'
'https://blog.naver.com/wjdwngkdsla'
'https://blog.naver.com/wjdwngkdsla/221884221493'
'https://blog.naver.com/wjdwngkdsla/221884221493'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B8%B0%EC%B4%88'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%9C%A0%ED%8A%9C%EB%B2%84%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC%ED%95%A8%EC%88%98'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B3%80%EC%88%98'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%8A%AC%EA%B8%B0%EB%A1%9C%EC%9A%B4%EC%9D%98%EC%82%AC%EC%83%9D%ED%99%9C'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9%EC%B4%88%EB%B3%B4'
'https://blog.naver.com/jslee3929'
'https://blog.naver.com/jslee3929'
'https://blog.naver.com/jslee3929/222176640269'
'https://blog.naver.com/jslee3929/222176640269'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EA%B0%95%EC%9D%98%EB%85%B8%ED%8A%B8'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EA%B8%B0%EB%B3%B8%ED%8E%B8'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B0%95%EC%9D%98'
'https://blog.naver.com/jslee3929/222180639154'
'https://blog.naver.com/pauseand/221502721283'
'https://blog.naver.com/pauseand'
'https://blog.naver.com/pauseand'
'https://blog.naver.com/pauseand/221502721283'
'https://blog.naver.com/pauseand/221502721283'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%9D%B4%EB%A7%88%ED%8A%B8%ED%95%98%EB%82%A8%EC%A0%90'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EB%AC%B8%ED%99%94%EC%84%BC%ED%84%B0'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EB%B9%99%EA%B8%80%EC%97%90%EC%8A%A4'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%9E%90%EC%9C%A8%EC%A3%BC%ED%96%89'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EB%93%9C%EB%A1%A0%EB%A0%88%EC%9D%B4%EC%84%9C'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%97%90%EB%93%80%EB%B0%94%EC%9D%B4'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EB%AF%B8%EB%9E%98%EA%B5%90%EC%9C%A1'
'https://search.naver.com/search.naver?where=view&sm=tab_viw.all&query=%EC%BD%94%EB%94%A9%EB%A1%9C%EB%B4%87'
'https://search.naver.com/search.naver?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&nso=&where=view&sm=tab_nmr&mode=normal'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://coding.yah.ac/'
'https://coding.yah.ac/'
'https://coding.yah.ac/'
'https://coding.yah.ac/'
'https://spartacodingclub.kr/'
'https://spartacodingclub.kr/'
'https://spartacodingclub.kr/'
'https://spartacodingclub.kr/curriculum/web'
'https://spartacodingclub.kr/portfolio'
'https://spartacodingclub.kr/review'
'https://spartacodingclub.kr/online/webplus'
'https://spartacodingclub.kr/online/sql'
'https://spartacodingclub.kr/online/app'
'https://spartacodingclub.kr/'
'https://programmers.co.kr/learn/courses/28'
'https://programmers.co.kr/learn/courses/28'
'https://programmers.co.kr/learn/courses/28'
'https://programmers.co.kr/learn/courses/28'
'http://www.yes24.com/Product/Goods/56783566'
'http://www.yes24.com/Product/Goods/56783566'
'http://www.yes24.com/Product/Goods/56783566'
'http://www.yes24.com/Product/Goods/56783566'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=2&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=1&where=web'
'javascript:;'
'https://audioclip.naver.com/channels/1388/clips/103'
'https://audioclip.naver.com/channels/1388'
'javascript:;'
'https://audioclip.naver.com/channels/1388/clips/104'
'https://audioclip.naver.com/channels/1388'
'javascript:;'
'https://audioclip.naver.com/channels/1388/clips/77'
'https://audioclip.naver.com/channels/1388'
'https://audioclip.naver.com/search/episodes?keyword=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://kin.naver.com/qna/question.nhn'
'https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=1040101&docId=368456977&qb=64KY64+E7L2U65Sp&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0'
'https://kin.naver.com/search/one2oneLink?dirId=1040101&docId=368456977&answerNo=2'
'https://kin.naver.com/search/profileLink?dirId=1040101&docId=368456977&answerNo=2'
'https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=1040101&docId=368456977&qb=64KY64+E7L2U65Sp&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0'
'https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=1040101&docId=368460628&qb=64KY64+E7L2U65Sp&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0'
'https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=102020101&docId=115199866&qb=64KY64+E7L2U65Sp&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=kin&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9%20age&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall'
'https://search.naver.com/search.naver?where=kin&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9%20what&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall'
'https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=339710614&qb=64KY64+E7L2U65Sp&enc=utf8&section=kin.ext&rank=2&search_sort=0&spq=0'
'https://kin.naver.com/search/one2oneLink?dirId=10402&docId=339710614&answerNo=2'
'https://kin.naver.com/search/profileLink?dirId=10402&docId=339710614&answerNo=2'
'https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=339710614&qb=64KY64+E7L2U65Sp&enc=utf8&section=kin.ext&rank=2&search_sort=0&spq=0'
'https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10406&docId=372830218&qb=64KY64+E7L2U65Sp&enc=utf8&section=kin.ext&rank=3&search_sort=0&spq=0'
'https://kin.naver.com/search/one2oneLink?dirId=10406&docId=372830218&answerNo=1'
'https://kin.naver.com/search/profileLink?dirId=10406&docId=372830218&answerNo=1'
'https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10406&docId=372830218&qb=64KY64+E7L2U65Sp&enc=utf8&section=kin.ext&rank=3&search_sort=0&spq=0'
'https://search.naver.com/search.naver?where=kin&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&sm=tab_nmr'
'http://cafe.naver.com/zbook/2828'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://nid.naver.com/nidlogin.login?svctype=262144'
'http://cafe.naver.com/zbook/2828'
'http://cafe.naver.com/zbook'
'http://blog.naver.com/firekokuma2/222132369230?rvid=D1632D5BBED048E91ACA56E9BE4B1EE33E3D'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://nid.naver.com/nidlogin.login?svctype=262144'
'http://blog.naver.com/firekokuma2/222132369230?rvid=D1632D5BBED048E91ACA56E9BE4B1EE33E3D'
'http://blog.naver.com/firekokuma2'
'https://tv.naver.com/v/17513152'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://nid.naver.com/nidlogin.login?svctype=262144'
'https://tv.naver.com/v/17513152'
'https://tv.naver.com/narangna'
'https://www.youtube.com/watch?v=-jRSXLKm1v4'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://nid.naver.com/nidlogin.login?svctype=262144'
'https://www.youtube.com/watch?v=-jRSXLKm1v4'
'https://www.youtube.com/channel/UCwXo4SrEekae2qQA2XRBQzw'
'https://search.naver.com/search.naver?where=video&ie=utf8&nso=&sm=tab_nmr&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9'
'https://search.naver.com/search.naver?query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&sm=tab_pge&where=nexearch'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=2&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=1&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=3&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=11&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=4&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=21&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=5&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=31&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=6&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=41&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=7&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=51&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=61&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=9&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=71&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=10&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=81&where=web'
'https://search.naver.com/search.naver?display=10&f=&filetype=0&page=11&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9&research_url=&sm=tab_pge&start=1&where=web'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EA%B9%80%EC%A7%84%EC%9A%B1+%EC%9D%B4%EA%B1%B4%EB%A6%AC'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EA%B3%B5%EC%88%98%EC%B2%98%EC%9E%A5+%ED%9B%84%EB%B3%B4'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EB%98%90+%EB%A7%88%EC%95%BD+%ED%98%90%EC%9D%98%EB%A1%9C+%EC%9E%85%EA%B1%B4'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EC%9E%90%EA%B0%80%EA%B2%A9%EB%A6%AC+%EC%A4%91+%EC%83%9D%EC%9D%BC%ED%8C%8C%ED%8B%B0'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EC%9C%A0%ED%8A%9C%EB%B2%84+%EA%B5%AD%EA%B0%80%EB%B9%84'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EB%82%B4%EB%85%84+2%EC%9B%94%EB%B6%80%ED%84%B0+%EB%B0%B1%EC%8B%A0+%EC%A0%91%EC%A2%85'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EB%B0%B1%EC%8B%A0+%EC%A0%91%EC%A2%85+%EC%8B%9C%EC%9E%91%EB%90%90%EC%A7%80%EB%A7%8C'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EB%82%A8%EC%96%91%EC%9C%A0%EC%97%85+%EC%99%B8%EC%86%90%EB%85%80+%ED%99%A9%ED%95%98%EB%82%98'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EC%A7%91%ED%96%89%EC%9C%A0%EC%98%88+%EC%A4%91%EC%97%90'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.nws&ie=utf8&query=%EA%B9%80%EA%B7%BC%EC%8B%9D+%EC%84%9C%EC%9A%B8%EC%8B%9C%EC%9E%A5+%EC%B6%9C%EB%A7%88'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%EA%B9%80%EB%AA%85%EC%88%98+%EC%9E%85%EB%8C%80'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%EC%A0%95%EA%B2%BD%EB%AF%B8+%EC%9C%A4%ED%98%95%EB%B9%88'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%EB%9D%BC%EC%9D%B8%EC%97%85+%EA%B3%B5%EA%B0%9C'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%EC%95%84%EB%A6%84%EB%8B%A4%EC%9B%A0%EB%8D%98+%EC%9A%B0%EB%A6%AC%EC%97%90%EA%B2%8C+%EC%86%8C%EC%A3%BC%EC%97%B0'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%ED%8E%9C%ED%8A%B8%ED%95%98%EC%9A%B0%EC%8A%A4+%EC%9D%B4%EC%A7%80%EC%95%84'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=2020+KBS+%EC%97%B0%EA%B8%B0%EB%8C%80%EC%83%81+%EC%8A%A4%ED%8E%98%EC%85%9C+MC'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%EB%B9%84%EA%B8%B4%EC%96%B4%EA%B2%8C%EC%9D%B8+%EC%98%A4%ED%94%88%EB%A7%88%EC%9D%B4%ED%81%AC'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%EC%97%91%EC%86%8C+%EB%94%94%EC%98%A4+1%EC%9B%94+25%EC%9D%BC+%EB%AF%B8%EB%B3%B5%EA%B7%80+%EC%A0%84%EC%97%AD'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%EB%AA%A8%EB%AA%A8%EB%9E%9C%EB%93%9C+%EB%82%B8%EC%8B%9C+10%EC%9C%84'
'https://search.naver.com/search.naver?where=nexearch&sm=tab_htk.ent&ie=utf8&query=%EC%86%A1%EA%B0%80%EC%9D%B8+%ED%8C%AC%ED%81%B4%EB%9F%BD'
'https://help.naver.com/support/alias/search/word/word_3.naver'
'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9#'
'https://www.naver.com/more.html'
'https://policy.naver.com/policy/service.html'
'https://policy.naver.com/policy/privacy.html'
'https://help.naver.com/support/alias/search/integration/integration_1.naver'
'https://www.navercorp.com/'
>>>
>>>
>>>
>>>
>>>
>>> browser.get("http://daum.net")
>>> elem = browser.find_element_by_name("q")
>>>
>>> elem
<selenium.webdriver.remote.webelement.WebElement (session="8c60d30a5c2380631cb29b3f8e8fb118", element="ad944a8a-33a7-4752-ad34-6375cc122f94")>
>>>
>>> elem.send_keys("나도코딩")
>>> elem.send_keys(Keys.ENTER)
>>> browser.back()
>>> elem.send_keys("나도코딩")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\양지철\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\webelement.py", line 477, in send_keys
    self._execute(Command.SEND_KEYS_TO_ELEMENT,
  File "C:\Users\양지철\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Users\양지철\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\양지철\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
  (Session info: chrome=87.0.4280.88)

>>> elem = browser.find_element_by_name("q")
>>> elem.send_keys("나도코딩")
>>> \
...
>>>
>>>
>>> elem = browser.fine_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'WebDriver' object has no attribute 'fine_element_by_xpath'
>>> elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
>>>
>>> elem
<selenium.webdriver.remote.webelement.WebElement (session="8c60d30a5c2380631cb29b3f8e8fb118", element="d51be4e2-a16f-485a-bdf8-59177a3cf104")>
>>> elem.click()
>>> browser.quit()
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> exit()
