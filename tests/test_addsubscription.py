import json

import pytest

from PageObjects.Homepage import Homepage
from PageObjects.LoginPage import Login
from PageObjects.Offerselection import OfferSelection
from PageObjects.Submission import Submission

with open("../testdata/dadtpack_addsubscription.json") as f:
    addsub_data = json.load(f)
    datpack_data = addsub_data["data"]
    topup_data=addsub_data["topup"]


@pytest.mark.parametrize("list_of_data", datpack_data)
def test_data_packs_addsusbription(invoke_browser, list_of_data):
    driver = invoke_browser
    loginpage = Login(driver)
    loginpage.login(list_of_data["username"], list_of_data["password"])
    homepage = Homepage(driver)
    homepage.punchin_number(list_of_data["msisdn"])
    homepage.find_menus()
    offerselection = OfferSelection(driver)
    offerselection.data_offer_selection(list_of_data["plan"])
    submission = Submission(driver)
    submission.submission_page("Your order is being processed.", "Unable to Process",
                               f"C:\\Users\\sanjay.ravisha.STS\\PycharmProjects\\REvision_Framework\\Reports\\{list_of_data["plan"]}_sucess.png",
                               f"C:\\Users\\sanjay.ravisha.STS\\PycharmProjects\\REvision_Framework\\Reports\\{list_of_data["plan"]}_failure.png")


@pytest.mark.smoke
@pytest.mark.parametrize("topup_data", topup_data)
def test_topup_packs_addsusbription(invoke_browser, topup_data):
    driver = invoke_browser
    loginpage = Login(driver)
    loginpage.login(topup_data["username"], topup_data["password"])
    homepage = Homepage(driver)
    homepage.punchin_number(topup_data["msisdn"])
    homepage.find_topup_menus()
    offerselection = OfferSelection(driver)
    offerselection.top_up_offer_selection(topup_data["plan"])
    submission = Submission(driver)
    submission.submission_page("Your order is being processed.", "Unable to Process",
                               f"C:\\Users\\sanjay.ravisha.STS\\PycharmProjects\\REvision_Framework\\Reports\\{topup_data["plan"]}_sucess.png",
                               f"C:\\Users\\sanjay.ravisha.STS\\PycharmProjects\\REvision_Framework\\Reports\\{topup_data["plan"]}_failure.png")