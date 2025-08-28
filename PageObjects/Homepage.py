import json
import time
from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.enter_msisdn = (By.XPATH, '//input[@name="customerMobNumber"]')
        self.proceed = (By.XPATH, '//button[text()="Proceed"]')
        self.menus = (By.CSS_SELECTOR, ".retailer-menu-item")
        self.past_transaction_search=(By.XPATH,'//input[@name="searchData"]')
        self.exp_wait = WebDriverWait(self.driver, 10)


    def punchin_number(self, msisdn):
        self.exp_wait.until(
            expected_conditions.presence_of_element_located(self.enter_msisdn)).send_keys(msisdn)
        wallet_balnce = self.driver.find_element(By.CSS_SELECTOR, ".wallet-balance-text").text
        inital_balance=Decimal(wallet_balnce.replace('$', '').replace(',', '').strip())
        self.driver.find_element(*self.proceed).click()
        return inital_balance

    def find_menus(self):
        menus = self.exp_wait.until(expected_conditions.presence_of_all_elements_located(self.menus))
        for i in menus:
            if i.text == 'Data & Roaming':
                i.click()


    def find_topup_menus(self):
        menus = self.exp_wait.until(expected_conditions.presence_of_all_elements_located(self.menus))
        time.sleep(3)
        for i in menus:
            if i.text == 'Top Up':
                i.click()


    def find_Add_ons_menus(self):
        menus = self.exp_wait.until(expected_conditions.presence_of_all_elements_located(self.menus))
        time.sleep(2)
        for i in menus:
            if i.text == 'Add-ons':
                i.click()

    def past_transaction(self,msisdn):
        self.driver.find_element(By.XPATH, "//span[text()='Past Transactions']").click()
        self.exp_wait.until(expected_conditions.presence_of_element_located(self.past_transaction_search)).send_keys(msisdn)
        self.driver.find_element(By.CSS_SELECTOR, ".absolute.right-2.top-4").click()
        purchased_offers=self.exp_wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, '//div[@class="retailer-transaction-table mt-10"]')))
        self.driver.save_screenshot("../Reports/past_transaction.png")
        for i in purchased_offers:
            offer_purchased_time=i.find_element(By.XPATH, 'div/div[3]/div').text
            break
        return offer_purchased_time

