from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import chromedriver_binary
import urllib.parse

from .config import *


class AutoLiker:

    def __init__(self, *, username, password, hashtag, max_like_count=10):
        self.username = username
        self.password= password
        self.hashtag = hashtag
        self.max_like_count = max_like_count

        self.like_count = 0

        options = Options()
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)


    def start(self):
        self.login()
        self.likes()

    def login(self):
        try:
            self.driver.get(INSTAGRAM_LOGIN_URL)

            auth_inputs = self.find_by_class_name(CLASS_NAME_AUTH)
            if len(auth_inputs) >= 2:
                username_input = auth_inputs[0]
                password_input = auth_inputs[1]
                username_input.send_keys(self.username)
                password_input.send_keys(self.password)
                password_input.send_keys(Keys.RETURN)
                print('Logged in Success !!')
        
            # 通知をONにするのポップアップが出る可能性を考慮
                try:
                    mention_popup_close = self.find_by_class_name(CLASS_NAME_MENTION_CLOSE)[0].click()
                except:
                   print('Popup Close Failed !!') 
        except:
            print('Logged In Failed !!')

    def likes(self):
        try:
            search_url = INSTAGRAM_TAG_SEARCH_URL.format(urllib.parse.quote(self.hashtag))
            self.driver.get(search_url)

            self.find_by_class_name(CLASS_NAME_MEDIA)[0].click()

            self.like_count = 0
            while self.like_count < self.max_like_count:
                # いいねボタンが押下済みでないか確認
                like_span_label = self.driver.find_by_class_name(CLASS_NAME_FAVO_SPAN)[0]
                print(like_span_label)
                break

                try:
                    self.find_by_class_name(CLASS_NAME_FAVO)[0].click()
                    self.like_count += 1
                    self.find_by_class_name(CLASS_NAME_NEXT)[0].click()
                except:
                    break
        except:
            print('Likes Failed !!')


    def find_by_class_name(self, class_name):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
        return self.driver.find_elements_by_class_name(class_name)
    
    def get_result(self):
        return {
            'hashtag': self.hashtag,
            'like_count': self.like_count,
        }
