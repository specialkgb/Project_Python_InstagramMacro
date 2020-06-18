# * hashtag_reply_macro.py
#
#

from selenium import webdriver
import time, random
from bs4 import BeautifulSoup

# 1.Chrome Driver Setup
path = '..'
driver = webdriver.Chrome(executable_path='{}/webdriver/chromedriver.exe'.format(path))

# 2.Instagram Login
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver.get(url)
time.sleep(3)

# what is xpath?
# : XPath는 W3C의 표준으로 확장 생성언어 문서의 구조를 통해 경로 위에
# 지정한 구문을 사용하여 항목을 배치하고 처리하는 방법을 기술하는 언어
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

# 3.HashTag Searching
time.sleep(2)
hash_url = 'https://www.instagram.com/explore/tags/bmwi8/'
driver.get(hash_url)

# 4.Board List Input & Output
def parse(page_code):
    soup = BeautifulSoup(page_code, 'html.parser')
    feed_list = soup.findAll('div', {'class','v1Nh3'}) # class값은 수시로 변경됨(실행할 때마다 확인!)

    links = []
    for one in feed_list:
        insta_link = 'https://www.instagram.com'
        link_Addr = one.find('a')['href']
        print(insta_link + link_Addr)
        links.append(insta_link + link_Addr)
    return links

time.sleep(4)
page_code = driver.page_source
links = parse(page_code)
print('Feed Cnt:', len(links))

# 좋아요 누르고 댓글 달기
for url in links:
    try:
        driver.get(url)

        rnd_sec = random.randint(5, 15)
        time.sleep(rnd_sec)
        message = 'What a nice car!'

        # 좋아요
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()

        # 댓글
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys(message)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/button').click()
    except Exception as e:
        print(e)