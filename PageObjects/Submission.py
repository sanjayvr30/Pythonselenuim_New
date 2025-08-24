import time

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
        if submission_message == sucess_message:
            exp_wait.until(expected_conditions.element_to_be_clickable(self.okay_button)).click()
            # self.driver.find_element(*self.okay_button).click()
            exp_wait.until(
                expected_conditions.presence_of_element_located(self.payment_recived))
            self.driver.save_screenshot(sucess_screenshopt_path)
            self.driver.find_element(*self.okay_button).click()
        if submission_message == failure_message:
            self.driver.save_screenshot(failure_screenshopt_path)
            self.driver.find_element(*self.okay_button).click()
        time.sleep(5)
