import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Offerselection import OfferSelection


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.enter_msisdn = (By.XPATH, '//input[@name="customerMobNumber"]')
        self.proceed = (By.XPATH, '//button[text()="Proceed"]')
        self.menus = By.CSS_SELECTOR, ".retailer-menu-item"
        self.exp_wait = WebDriverWait(self.driver, 10)

    def punchin_number(self, msisdn):

        self.exp_wait.until(
            expected_conditions.presence_of_element_located(self.enter_msisdn)).send_keys(msisdn)
        self.driver.find_element(*self.proceed).click()

    def find_menus(self):
        menus = self.exp_wait.until(expected_conditions.presence_of_all_elements_located(self.menus))
        # menus = self.driver.find_elements(*self.menus)
        # print(menus)
        for i in menus:
            if i.text == 'Data & Roaming':
                i.click()


    def find_topup_menus(self):
        menus = self.exp_wait.until(expected_conditions.presence_of_all_elements_located(self.menus))
        time.sleep(2)
        for i in menus:
            if i.text == 'Top Up':
                i.click()