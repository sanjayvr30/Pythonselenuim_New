from selenium.webdriver.common.by import By

from PageObjects.Optpage import Otppage


class Login:

    def __init__(self,driver):
        self.driver= driver
        self.username=(By.XPATH, '//input[@name="phoneNumber"]')
        self.password=(By.XPATH, '//input[@name="password"]')
        self.click_login_button=(By.XPATH, '//button[text()="Send OTP"]')


    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.click_login_button).click()
        otppage=Otppage(self.driver)
        return otppage.enter_opt("0")