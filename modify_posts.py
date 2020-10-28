#!/usr/bin/env python3
"""Paginate 기능 테스트용dummy post 생성 혹은 삭제를 위한 파일
"""


import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


DRIVER_PATH = "./chromedriver"
BLOG_URL = "localhost:5000"
BLOG_EMAIL = os.environ.get('BLOG_EMAIL')
BLOG_PASSWORD = os.environ.get('BLOG_PASSWORD')

def write_posts(count=26):
    for i in range(1, count):
        driver.find_element(By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[1]').click()
        driver.find_element(By.XPATH, '//*[@id="title"]').send_keys(f"Paginate Test {i}")
        driver.find_element(By.XPATH, '//*[@id="content"]')\
                .send_keys(f'Paginate 테스트를 위한 게시글 {i}번 입니다.')

        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        time.sleep(0.1)

def delete_posts(count=26):
    for i in range(1, count):
        time.sleep(1)
        article = driver.find_element(By.XPATH,
                                      f'/html/body/main/div/div[1]/article[{i}]/div/h2/a')
        # TODO: 페이지가 완전히 로드된 후 클릭되는 기능 추가하기
        if 'Paginate' in article.text:
            article.click()
            driver.find_element(By.XPATH,
                                '/html/body/main/div/div[1]/article/div/div/div/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,
                                '//*[@id="deleteModal"]/div/div/div[2]/form/input').click()
            time.sleep(0.5)



if __name__ == "__main__":
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BLOG_URL)

    login_btn = driver.find_element(By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[1]')
    login_btn.click()

    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys(BLOG_EMAIL)
    time.sleep(0.1)
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys(BLOG_PASSWORD)
    time.sleep(0.1)

    login = driver.find_element(By.XPATH, '//*[@id="submit"]')
    login.click()
    time.sleep(0.1)

    write_posts()
    # delete_posts()



        




