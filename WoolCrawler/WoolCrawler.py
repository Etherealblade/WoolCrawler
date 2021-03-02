'''
Description: Capturing bandwidth of vps

Ref to: 
https://www.hongkiat.com/blog/automate-create-login-bot-python-selenium/
https://blog.csdn.net/lixianlin/article/details/80866598

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import *
import os


def capture():
    # ============ Step 1: Login ============
    usernameStr = '*'   # 此处自行修改
    passwordStr = '*'

    # fill in username and pwd
    browser = webdriver.Firefox()
    browser.get('https://juzicloud.net/user')
    username = browser.find_element_by_id('email')
    username.send_keys(usernameStr)
    password = browser.find_element_by_id('password')
    password.send_keys(passwordStr)
 
    signInButton = browser.find_element_by_css_selector(".btn-primary")
    signInButton.click()

    # ======== Step 2: Click the "签到" button ========
    sleep(3)   # Waiting for refreshing the webpage
    signInButton = browser.find_element_by_id('checkin-div')
    signInButton.click()


if __name__ == "__main__":
    # Proxy setting
    os.environ["http_proxy"] = "http://127.0.0.1:10809"
    os.environ["https_proxy"] = "http://127.0.0.1:10809"

    capture()