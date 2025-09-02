from PageObjects.Homepage import Homepage
from PageObjects.LoginPage import Login


def test_change_language(invoke_browser):
    driver=invoke_browser
    loginpage=Login(driver)
    loginpage.login("bfn175","Admin@123456")
    homepage=Homepage(driver)
    homepage.change_language()


