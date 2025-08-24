from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Homepage import Homepage


class Otppage:

    def __init__(self, driver):
        self.driver = driver
        self.verify_otp = (By.XPATH, '//button[text()="Verify"]')

    def enter_opt(self,otp):
        exp_wait = WebDriverWait(self.driver, 10)
        for i in range(1, 7):
            exp_wait.until(expected_conditions.presence_of_element_located(
                (By.XPATH, f'//input[@aria-label="Please enter OTP character {i}"]'))).send_keys(otp)
        self.driver.find_element(*self.verify_otp).click()
