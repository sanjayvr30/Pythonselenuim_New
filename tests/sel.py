import time

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import requests


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://theobroma.in/collections/cakes")
print(driver.title)
print(driver.current_url)
respose=requests.get("https://theobroma.in/collections/cakes")
print(respose.status_code)



#
# opned_windows=driver.window_handles
# driver.switch_to.window(opned_windows[0])
# driver.find_element("name", "Cake")
#
#
# driver.get_tittle
# alert=driver.switch_to.alert
# alert.accept()
# alert.text
# alert.dismiss()
# alert.send_keys(
#
# )
# cakes=driver.find_elements(By.XPATH, '//div[@class="row"]//div/div/div/div[3]/span/h3[1][a]')
# for i in cakes:
#     # print(i.text)
#     # print("=============")
#     if "Cake" in i.text:
#         print(i.text)
#
#
#
#
# try:
#     a=1
#     b=2
#     c=4
#     assert a+b==c, "Sum is wrong"
# except Exception as e:
#     print(f"Exception: {e}")
















#
# driver = webdriver.Chrome()
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver.maximize_window()
# driver.get("https://domo-eload-uat.m1.com.sg/login")
# exp_wait = WebDriverWait(driver, 10)
# time.sleep(3)
# driver.find_element(By.XPATH, '//input[@name="phoneNumber"]').send_keys("bfn175")
# driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Admin@123456")
# driver.find_element(By.XPATH, '//button[text()="Send OTP"]').click()
# # time.sleep(3)
# for i in range(1, 7):
#     exp_wait.until(expected_conditions.presence_of_element_located(
#         (By.XPATH, f'//input[@aria-label="Please enter OTP character {i}"]'))).send_keys("0")
#     # driver.find_element(By.XPATH, f'//input[@aria-label="Please enter OTP character {i}"]').send_keys("0")
# driver.find_element(By.XPATH, '//button[text()="Verify"]').click()
# exp_wait.until(
#     expected_conditions.presence_of_element_located((By.XPATH, '//input[@name="customerMobNumber"]'))).send_keys(
#     "21001322")
# # driver.find_element(By.XPATH, '//button[@name="customerMobNumber"]').send_keys("21001322")
# driver.find_element(By.XPATH, '//button[text()="Proceed"]').click()
# menus = driver.find_elements(By.CSS_SELECTOR, ".retailer-menu-item")
# lis = []
# for i in menus:
#     # print(i.text)
#     if i.text == 'Data & Roaming':
#         i.click()
# exp_wait.until(
#     expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Data Packs - 30 Days']"))).click()
# offers = driver.find_elements(By.XPATH, "//div[@class='block']/div/div[2]")
# for i in offers:
#     offer_name = i.find_element(By.XPATH, 'div/span[1]')
#     if offer_name.text == "100GB Data Pack":
#         offer_price = i.find_element(By.XPATH, 'div/span[2]')
#         print(offer_price.text)
#         i.find_element(By.XPATH, 'div[4]/button').click()
# driver.find_element(By.CSS_SELECTOR, ".retailer-balance-modal-header.font-bold.text-custum-orange-500")
# driver.find_element(By.XPATH, '//button[text()="Proceed to pay"]').click()
# submission_message = exp_wait.until(expected_conditions.presence_of_element_located(
#     (By.CSS_SELECTOR, ".text-center.retailer-balance-modal-header"))).text
# if submission_message == "Your order is being processed.":
#     driver.find_element(By.XPATH, "//button[text()='Okay']").click()
#     exp_wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[text()='Payment received!']")))
#     driver.save_screenshot("C:\\Users\\sanjay.ravisha.STS\\PycharmProjects\\REvision_Framework\\Reports\\aimage.png")
#     driver.find_element(By.XPATH, "//button[text()='Okay']").click()
# if submission_message == "Unable to Process":
#     driver.save_screenshot("C:\\Users\\sanjay.ravisha.STS\\PycharmProjects\\REvision_Framework\\Reports\\failure")
#     driver.find_element(By.XPATH, "//button[text()='Okay']").click()
# time.sleep(5)
