from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

enterpriseId = raw_input("Please enter you enterprise Id: ")
pw = raw_input("Please enter your password: ")
s_code = raw_input("please enter your 6 digits security code: ")

browser = webdriver.Chrome()
browser.get("http://myte.accenture.com")

username = browser.find_element_by_css_selector("#userNameInput")
password = browser.find_element_by_css_selector("#passwordInput")

username.send_keys(enterpriseId)
password.send_keys(pw)

browser.find_element_by_css_selector("#submitButton").click()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "otpInput"))
    )
    security_code = browser.find_element_by_css_selector("#otpInput")
    security_code.send_keys(s_code)
    browser.find_element_by_css_selector("#vipSubmitOTP").click()
except RuntimeError:
    print("error opening up security login page")

