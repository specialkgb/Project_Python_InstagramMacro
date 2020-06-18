# * chapter02_webdriver.py
# * : Selenium의 Webdriver 사용방법(+Chrome Driver)
# * :
# *

from selenium import webdriver

# instagram 페이지에서 원하는 해쉬태그로 selenium 접속(+ 크롬 드라이버)
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')
# https://www.instagram.com/explore/tags/bmwi8/
# URL 주소의 한글은 유니코드로 변환(한글이면 깨지는 경우가 있음)

url = 'https://www.instagram.com/explore/tags/bmwi8/'
driver.get(url)
# driver.close() # 실행 후 브라우저 종료