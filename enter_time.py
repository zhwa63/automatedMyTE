from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# enterpriseId = raw_input("Please enter you enterprise Id: ")
# pw = raw_input("Please enter your password: ")
s_code = raw_input("please enter your 6 digits security code: ")

browser = webdriver.Chrome()
browser.get("http://myte.accenture.com")

username = browser.find_element_by_css_selector("#userNameInput")
password = browser.find_element_by_css_selector("#passwordInput")

# username.send_keys(enterpriseId)
# password.send_keys(pw)

browser.find_element_by_css_selector("#submitButton").click()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "otpInput"))
    )

except RuntimeError:
    print("Time out when opening up security login page")

security_code = browser.find_element_by_css_selector("#otpInput")
security_code.send_keys(s_code)
browser.find_element_by_css_selector("#vipSubmitOTP").click()

# Enter myTE main page
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "TutorialPopUpControl_btnClose"))
    )

except RuntimeError:
    print("Time out when directing to myTE")

# Close tutorial popup
browser.find_element_by_css_selector("#TutorialPopUpControl_chkNeverShowAgain").click()
browser.find_element_by_css_selector("#TutorialPopUpControl_btnClose").click()
browser.find_element_by_css_selector("#myTime_Card > div.header > h2 > a").click()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "WorkingHoursMenuLink"))
    )

except RuntimeError:
    print("Time out when directing to time sheet")

browser.find_element_by_css_selector("#WorkingHoursMenuLink").click()
print("frame num after click", len(browser.find_elements_by_tag_name("iframe")))

try:
    element = WebDriverWait(browser, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "DynamicPopupIframe"))
    )
except RuntimeError:
    print("Time out when switching the iframe")

print("frame num after switch", len(browser.find_elements_by_tag_name("iframe")))
print("select num after switch", len(browser.find_elements_by_tag_name("form")))
# browser.find_element_by_css_selector("#btn_Cancel").click()
# select = Select(browser.find_element_by_css_selector("#ctl00_PopupContentPlaceHolder_wdgWorkingHoursEntry_ctl02_StartWorkTimeDropDown"))
# print(select.options)
# select.select_by_value("09 AM")

# driver.switch_to.window(main_window_handle)



