import time
from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Submission:

    def __init__(self, driver):
        self.driver = driver
        self.submission_text = (By.CSS_SELECTOR, ".text-center.retailer-balance-modal-header")
        self.okay_button = (By.XPATH, "//button[text()='Okay']")
        self.payment_recived = (By.XPATH, "//p[text()='Payment received!']")

    def submission_page(self, sucess_message, failure_message, sucess_screenshopt_path, failure_screenshopt_path):
        exp_wait = WebDriverWait(self.driver, 10)
        submission_message = exp_wait.until(expected_conditions.presence_of_element_located(
            self.submission_text)).text
        submission_time = None
        final_wallet_balance = None
        if submission_message == sucess_message:
            exp_wait.until(expected_conditions.element_to_be_clickable(self.okay_button)).click()
            exp_wait.until(
                expected_conditions.presence_of_element_located(self.payment_recived))
            self.driver.save_screenshot(sucess_screenshopt_path)
            submission_time = self.driver.find_element(By.XPATH, "//div/div[1]/div[3]/div[1]/span[2]").text
            self.driver.find_element(*self.okay_button).click()
            wallet_balance = exp_wait.until(expected_conditions.presence_of_element_located
                                            ((By.CSS_SELECTOR, ".wallet-balance-text"))).text
            final_wallet_balance = Decimal(wallet_balance.replace("$", "").replace(",", "").strip())
        if submission_message == failure_message:
            self.driver.save_screenshot(failure_screenshopt_path)
            self.driver.find_element(*self.okay_button).click()

        time.sleep(5)
        return submission_time, final_wallet_balance  # Return both values as tuple

    def submission_page(self, sucess_message, failure_message, sucess_screenshopt_path, failure_screenshopt_path):
        exp_wait = WebDriverWait(self.driver, 10)
        submission_message = exp_wait.until(expected_conditions.presence_of_element_located(
            self.submission_text)).text
        if submission_message == sucess_message:
            exp_wait.until(expected_conditions.element_to_be_clickable(self.okay_button)).click()
            exp_wait.until(
                expected_conditions.presence_of_element_located(self.payment_recived))
            self.driver.save_screenshot(sucess_screenshopt_path)
            submission_time=self.driver.find_element(By.XPATH, "//div/div[1]/div[3]/div[1]/span[2]").text
            self.driver.find_element(*self.okay_button).click()
            wallet_balance=exp_wait.until(expected_conditions.presence_of_element_located
                                         ((By.CSS_SELECTOR, ".wallet-balance-text"))).text
            final_wallet_balance=Decimal(wallet_balance.replace("$","").replace(",","").strip())
        if submission_message == failure_message:
            self.driver.save_screenshot(failure_screenshopt_path)
            self.driver.find_element(*self.okay_button).click()
        return final_wallet_balance,submission_time
        time.sleep(5)
