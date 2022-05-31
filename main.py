from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

username = 'Linkedin email/username'
password = 'Password'
url = 'https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python%20developer'

chrome_driver_path = Service('C:/development_chrome_driver/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get(url)
sign_in = driver.find_element(by=By.LINK_TEXT, value='Sign in')
sign_in.click()
username_input = driver.find_element(by=By.ID, value='username')
username_input.send_keys(username)
password_input = driver.find_element(by=By.ID, value='password')
password_input.send_keys(password)
sign_in_primary = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in_primary.click()
