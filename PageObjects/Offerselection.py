import time
from decimal import Decimal

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OfferSelection:

    def __init__(self, driver):
        self.driver = driver
        self.okay_button = (By.XPATH, "//button[normalize-space()='Okay']")
        self.find_offers = (By.XPATH, "//div[@class='block']/div/div[2]")
        self.offer_name = (By.XPATH, 'div[1]/span[1]')
        self.offer_price = (By.XPATH, 'div[1]/span[2]')
        self.comission_price = (By.XPATH, 'div[2]/span[2]')
        self.add_to_cart = (By.XPATH, 'div[4]/button')
        self.proceed_to_pay = (By.XPATH, '//button[text()="Proceed to pay"]')
        self.data_pack_menu = (By.XPATH, "//span[text()='Data Packs - 30 Days']")
        self.top_up_menu = (By.XPATH, "//span[text()='All-in-1']")
        self.add_on_menu = (By.XPATH, '//span[tex()="Validity Extension"]')
        self.first_top_up_offers = (By.XPATH, '//div[@class="md:mx-10 mb-10"]/div/div[2]')
        self.first_topup_offer_name = (By.XPATH, 'div[1]/span[1]')
        self.first_topup_buynow = (By.XPATH, 'div[4]/button')
        self.exp_wait = WebDriverWait(self.driver, 10)
        self.first_topup_offerprice = (By.XPATH, 'div[1]/span[2]')
        self.first_topup_comissionprice = (By.XPATH, 'div[2]/span[2]')

    def data_offer_selection(self, offername):
        self.exp_wait.until(
            expected_conditions.presence_of_element_located(
                self.data_pack_menu)).click()
        time.sleep(2)
        offers = self.driver.find_elements(*self.find_offers)
        for i in offers:
            offer_name = i.find_element(*self.offer_name)
            if offer_name.text == offername:
                offer_price = i.find_element(*self.offer_price).text
                price_decimal = Decimal(offer_price.replace('$', '').replace(',', '').strip())
                commision_price = i.find_element(*self.comission_price).text
                commision_decimal = Decimal(commision_price.replace('$', '').replace(',', '').strip())
                total_offer_price_with_comission = price_decimal - commision_decimal
                i.find_element(*self.add_to_cart).click()
            else:
                print("Offer didn't Match")
        self.driver.find_element(*self.proceed_to_pay).click()
        return total_offer_price_with_comission

    def top_up_offer_selection(self, offername):
        self.exp_wait.until(
            expected_conditions.presence_of_element_located(
                self.top_up_menu)).click()
        time.sleep(2)
        offers = self.driver.find_elements(*self.find_offers)
        for i in offers:
            offer_name = i.find_element(*self.offer_name)
            if offer_name.text == offername:
                offer_price = i.find_element(*self.offer_price).text
                price_decimal = Decimal(offer_price.replace('$', '').replace(',', '').strip())
                commision_price = i.find_element(*self.comission_price).text
                commision_decimal = Decimal(commision_price.replace('$', '').replace(',', '').strip())
                print(f"Commssion amount:{commision_decimal}")
                print(f"Offer amount:{price_decimal}")
                total_offer_price_with_comission = price_decimal - commision_decimal
                i.find_element(*self.add_to_cart).click()
            else:
                print("Offer didn't Match")
        self.driver.find_element(*self.proceed_to_pay).click()
        return total_offer_price_with_comission, price_decimal

    def add_On_selection(self, offername):
        self.exp_wait.until(
            expected_conditions.presence_of_element_located(
                self.add_on_menu)).click()
        time.sleep(2)
        offers = self.driver.find_elements(*self.find_offers)
        for i in offers:
            offer_name = i.find_element(*self.offer_name)
            if offer_name.text == offername:
                offer_price = i.find_element(*self.offer_price).text
                price_decimal = Decimal(offer_price.replace('$', '').replace(',', '').strip())
                commision_price = i.find_element(*self.comission_price).text
                commision_decimal = Decimal(commision_price.replace('$', '').replace(',', '').strip())
                total_offer_price_with_comission = price_decimal - commision_decimal
                i.find_element(*self.add_to_cart).click()
            else:
                print("Offer didn't Match")
        self.driver.find_element(*self.proceed_to_pay).click()
        return total_offer_price_with_comission

    def first_topup_offer(self, offername):
        actions = ActionChains(self.driver)
        offers = self.exp_wait.until(expected_conditions.presence_of_all_elements_located(self.first_top_up_offers))
        for i in offers:
            offer_name = i.find_element(*self.first_topup_offer_name).text
            print(offer_name)
            if offer_name == offername:
                i.find_element(*self.first_topup_buynow).click()
                offer_price = i.find_element(*self.first_topup_offerprice).text
                price_decimal = Decimal(offer_price.replace('$', '').replace(',', '').strip())
                commision_price = i.find_element(*self.first_topup_comissionprice).text
                commision_decimal = Decimal(commision_price.replace('$', '').replace(',', '').strip())
                total_offer_price_with_comission = price_decimal - commision_decimal
                i.find_element(*self.add_to_cart).click()
                actions.move_to_element(self.driver.find_element(By.XPATH, "//sapn[text()='Clear All']")).perform()
                self.driver.execute_script("window.scroll(0,1500);")
                self.driver.find_element(By.XPATH, "//path[@fill-rule='evenodd']").click()
                time.sleep(3)
                self.exp_wait.until(expected_conditions.element_to_be_clickable(self.proceed_to_pay)).click()
        return total_offer_price_with_comission, price_decimal
