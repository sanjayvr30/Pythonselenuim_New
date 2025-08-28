import json

import pytest

from PageObjects.LoginPage import Login


with open("../testdata/forgotpassword_data.json") as f:
    forgot_password_data= json.load(f)
    entries=forgot_password_data["data"]



@pytest.mark.parametrize("forgot_password_entries",entries)
def test_forgotpassword(invoke_browser, forgot_password_entries ):
    driver =invoke_browser
    login=Login(driver)
    login.forgotpassword(forgot_password_entries["username"], forgot_password_entries["msisdn"])
