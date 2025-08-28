from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Optpage import Otppage


class Login:

    def __init__(self,driver):
        self.driver= driver
        self.exp_wait = WebDriverWait(self.driver, 10)
        self.username=(By.XPATH, '//input[@name="phoneNumber"]')
        self.password=(By.XPATH, '//input[@name="password"]')
        self.click_login_button=(By.XPATH, '//button[text()="Send OTP"]')
        self.forgot_password_button=(By.XPATH, '//p[text()="Forgot Password"]')
        self.f_p_ursename=(By.CSS_SELECTOR, 'input[name="uname"]')
        self.f_p_number=(By.CSS_SELECTOR, 'input[name="uMobileNumber"]')
        self.submit_button=(By.XPATH, '//button[text()="Submit"]')

    # def login(self, **kwargs):
    #     self.driver.find_element(*self.username).send_keys(kwargs.get("username"))
    #     self.driver.find_element(*self.password).send_keys(kwargs.get("password"))
    #     self.driver.find_element(*self.click_login_button).click()
    #     # If you want to handle OTP dynamically
    #     otppage = Otppage(self.driver)
    #     return otppage.enter_opt("0")

    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.click_login_button).click()
        otppage=Otppage(self.driver)
        return otppage.enter_opt("0")

    def forgotpassword(self,username, msisdn):
        self.driver.find_element(*self.forgot_password_button).click()
        self.exp_wait.until(expected_conditions.presence_of_element_located(self.f_p_ursename)).send_keys(username)
        self.driver.find_element(*self.f_p_number).send_keys(msisdn)
        self.driver.find_element(*self.submit_button).click()
        sucess_text=self.exp_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//h3[text()="New Password Sent"]'))).text
        self.driver.save_screenshot("../Reports/resset_password.png")
        self.driver.find_element(By.XPATH, '//button[text()="Back to Log in"]').click()
        return sucess_text



