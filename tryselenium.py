from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(10)

def find_id(id):
    return driver.find_element(By.ID, id)


def find_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)


def find_xpaths(xpath):
    return driver.find_elements(By.XPATH, xpath)


def send(e, txt):
    e.send_keys(txt + Keys.RETURN)

def main1():
    from time import sleep
    driver.get('https://duckduckgo.com')
    print('Opened', 'https://duckduckgo.com')
    sleep(2)
    e = find_id('search_form_input')
    print('Found', 'search_form_input')
    sleep(2)
    send(e, 'selenium')
    print('Searched for', 'selenium')
    print('Test successful!')
    driver.quit()


def main2():
    driver.get('https://duckduckgo.com')
    print('Opened', 'https://duckduckgo.com')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ""))).send_keys('selenium'+Keys.RETURN)




if __name__ == '__main__':
    main2()
