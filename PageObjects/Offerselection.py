import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OfferSelection:

    def __init__(self, driver):
        self.driver = driver
        self.find_offers = (By.XPATH, "//div[@class='block']/div/div[2]")
        self.offer_name = (By.XPATH, 'div[1]/span[1]')
        self.offer_price = (By.XPATH, 'div[1]/span[2]')
        self.add_to_cart = (By.XPATH, 'div[4]/button')
        self.proceed_to_pay = (By.XPATH, '//button[text()="Proceed to pay"]')
        self.data_pack_menu = (By.XPATH, "//span[text()='Data Packs - 30 Days']")
        self.top_up_menu= (By.XPATH, "//span[text()='All-in-1']")

    def data_offer_selection(self, offername):
        exp_wait = WebDriverWait(self.driver, 10)
        exp_wait.until(
            expected_conditions.presence_of_element_located(
                self.data_pack_menu)).click()
        offers = self.driver.find_elements(*self.find_offers)
        for i in offers:
            offer_name = i.find_element(*self.offer_name)
            # print(offer_name.text)
            if offer_name.text == offername:
                offer_price = i.find_element(*self.offer_price)
                # print(offer_price.text)
                i.find_element(*self.add_to_cart).click()

        self.driver.find_element(*self.proceed_to_pay).click()


    def top_up_offer_selection(self, offername):
        exp_wait = WebDriverWait(self.driver, 10)
        exp_wait.until(
            expected_conditions.presence_of_element_located(
                self.top_up_menu)).click()
        time.sleep(3)
        offers = self.driver.find_elements(*self.find_offers)
        for i in offers:
            offer_name = i.find_element(*self.offer_name)
            if offer_name.text == offername:
                offer_price = i.find_element(*self.offer_price)
                print(offer_price.text)
                i.find_element(*self.add_to_cart).click()
            else:
                print("Offer didn't Match")
        self.driver.find_element(*self.proceed_to_pay).click()
