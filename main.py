from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random


driver = webdriver.Chrome()
driver.implicitly_wait(10)

task = True

MAIN_PAGE = "http://localhost:8081/"
driver.get(MAIN_PAGE)
try:
    for i in range(2):
        driver.find_element(By.XPATH, "//*[@id=\"carousel-banner-0\"]/button[2]").click()
    print("task 1 has successful")
except:
    print("task 1 has failed")
    task = False

try:
    driver.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/a").click()
    __import__("time").sleep(1)
    #euro
    driver.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[3]/a").click()
    
    driver.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/a").click()
    __import__("time").sleep(1)
    #dollar
    driver.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[3]/a")
    print("task 2 has successful")
except:
    print("task 2 has failed")
    task = False

try:
    driver.get(f"{MAIN_PAGE}/en-gb/catalog/desktops/pc")
    text = driver.find_element(By.XPATH, "//*[@id=\"content\"]/p[1]").text
    text_check = text == "There are no products to list in this category."
    if text_check:
        print("task 3 has successful")
except:
    print("task 3 has failed")
    task = False

numberEmail = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
try:
    driver.get(f"{MAIN_PAGE}/en-gb?route=account/register")
    account_field = driver.find_element(By.XPATH, "//*[@id=\"account\"]")
    account_field.find_element(By.NAME, "firstname").send_keys("Ivanov")
    account_field.find_element(By.NAME, "lastname").send_keys("Ivan")
    account_field.find_element(By.NAME, "email").send_keys(f"{numberEmail}@hmail.com")

    driver.find_element(By.NAME, "password").send_keys("Serata123!")
    time.sleep(1)
    checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    driver.execute_script("arguments[0].click();", checkbox)
    driver.find_element(By.XPATH, "//*[@id=\"form-register\"]/div/button").click()
    time.sleep(1)
    print("task 4 has succsesful")
except:
    print("task 4 has failed")
    task = False

try:
    driver.find_element(By.XPATH, "//*[@id=\"search\"]/input").send_keys("nothing phone")
    driver.find_element(By.XPATH, "//*[@id=\"search\"]/button").click()
    time.sleep(3)
    print("task 5 has succsessful")
except:
    print("task 5 has failed")
    task = False

if task:
    print("All task has done")
    
