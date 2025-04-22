from time import sleep
import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.nondestructive
def test_1(driver, base_url):
    driver.get(base_url)
    for _ in range(2):
        next_btn = driver.find_element(By.XPATH, "//*[@id=\"carousel-banner-0\"]/button[2]").click()
        sleep(0.5)
        active_slides = driver.find_elements(By.CSS_SELECTOR,'#carousel-banner-0 .carousel-item.active')
    assert len(active_slides) == 1, "Ожидался один активный слайд, но их больше"

@pytest.mark.nondestructive
def test_change_valute(driver, base_url):
    VALUTE_DISPLAY = "/html/body/nav/div/div[1]/ul/li[1]/form/div/a/strong"
    DROPTOWN_TUGGLE = "//*[@id=\"form-currency\"]/div/a"
    EURO = "//*[@id=\"form-currency\"]/div/ul/li[1]/a"
    POUND = "//*[@id=\"form-currency\"]/div/ul/li[2]/a"
    DOLLAR = "//*[@id=\"form-currency\"]/div/ul/li[3]/a"

    # euro
    driver.get(base_url)
    driver.find_element(By.XPATH, DROPTOWN_TUGGLE).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, EURO))).click()
    euro_present = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, VALUTE_DISPLAY),"€"))
    assert euro_present, "евро не отображается на странице"
    
    displayed = driver.find_element(By.XPATH, VALUTE_DISPLAY).text
    assert "€" in displayed, f"ожидалось '€', но получили '{displayed}'"

    #Pound
    driver.get(base_url)
    driver.find_element(By.XPATH, DROPTOWN_TUGGLE).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, POUND))).click()
    pount_present = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, VALUTE_DISPLAY),"£"))
    assert pount_present, "фунты не отображается на странице"
    
    displayed = driver.find_element(By.XPATH, VALUTE_DISPLAY).text
    assert "£" in displayed, f"ожидалось '£', но получили '{displayed}'"

    #Dollar
    driver.get(base_url)
    dollar_present = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, VALUTE_DISPLAY),"$"))
    assert pount_present, "фунты не отображается на странице"
    
    displayed = driver.find_element(By.XPATH, VALUTE_DISPLAY).text
    assert "$" in displayed, f"ожидалось '$', но получили '{displayed}'"





@pytest.mark.nondestructive
def test_category_product(driver, base_url):
    EXPECTED_TEXT = "There are no products to list in this category."
    driver.get(f"{base_url}/en-gb/catalog/desktops/pc")
    text = driver.find_element(By.XPATH, "//*[@id=\"content\"]/p[1]").text
    assert text == EXPECTED_TEXT, f"ожидалось {EXPECTED_TEXT}, но получили {text}"


@pytest.mark.nondestructive
def test_registration(driver, base_url):
    NUMBER_EMAIL = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
    FIRST_NAME = "Ivanov"
    LAST_NAME = "Ivan"
    EMAIL = f"{NUMBER_EMAIL}@mail.com"
    PASSWORD = "Serata123"

    driver.get(base_url)

    driver.find_element(By.XPATH, "//*[@id=\"top\"]/div/div[2]/ul/li[2]/div/a").click()
    driver.find_element(By.XPATH, "//*[@id=\"top\"]/div/div[2]/ul/li[2]/div/ul/li[1]/a").click()
    sleep(0.5)
    account_field = driver.find_element(By.XPATH, "//*[@id=\"account\"]")
    account_field.find_element(By.NAME, "firstname").send_keys(FIRST_NAME)
    account_field.find_element(By.NAME, "lastname").send_keys(LAST_NAME)
    account_field.find_element(By.NAME, "email").send_keys(EMAIL)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    driver.execute_script("arguments[0].click();", checkbox)
    driver.find_element(By.XPATH, "//*[@id=\"form-register\"]/div/button").click()

    heading_locator = (By.XPATH, '//*[@id="content"]/h1')
    expected_text = "Your Account Has Been Created!"

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(heading_locator, expected_text),
        message=f"Заголовок не стал '{expected_text}'"
    )
    heading_text = driver.find_element(*heading_locator).text
    assert heading_text == expected_text, (
        f"Ожидали '{expected_text}', но получили '{heading_text}'"
    )


@pytest.mark.nondestructive
def test_main_search(driver, base_url):
    FOUND_PRODUCT = "nothing phone"
    EXPECTED_TEXT = "Products meeting the search criteria"

    driver.get(base_url)
    driver.find_element(By.XPATH, "//*[@id=\"search\"]/input").send_keys(FOUND_PRODUCT)
    driver.find_element(By.XPATH, "//*[@id=\"search\"]/button").click()
    text = driver.find_element(By.XPATH, "//*[@id=\"content\"]/h2").text
    assert EXPECTED_TEXT == text, f"ожидалось {EXPECTED_TEXT}, но получили {text}"