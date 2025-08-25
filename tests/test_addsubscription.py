import json

import pytest

from PageObjects.Homepage import Homepage
from PageObjects.LoginPage import Login
from PageObjects.Offerselection import OfferSelection
from PageObjects.Submission import Submission
from utils.Baseclass import Baseclass

with open("../testdata/dadtpack_addsubscription.json") as f:
    addsub_data = json.load(f)
    datpack_data = addsub_data["data"]
    topup_data=addsub_data["topup"]
    addon_Ons=addsub_data["Addon"]


@pytest.mark.parametrize("list_of_data", datpack_data)
def test_data_packs_addsusbription(invoke_browser, list_of_data):
    baseclass=Baseclass()
    log=baseclass.logging()
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
                               f"../Reports\\{list_of_data["plan"]}_sucess.png",
                               f"../Reports\\{list_of_data["plan"]}_failure.png")


@pytest.mark.smoke
@pytest.mark.parametrize("topup_data", topup_data)
def test_topup_packs_addsusbription(invoke_browser, topup_data):
    baseclass=Baseclass()
    log=baseclass.logging()
    driver = invoke_browser
    loginpage = Login(driver)
    loginpage.login(topup_data["username"], topup_data["password"])
    homepage = Homepage(driver)
    inital_balance=homepage.punchin_number(topup_data["msisdn"])
    homepage.find_topup_menus()
    offerselection = OfferSelection(driver)
    total_offer_price_with_comission=offerselection.top_up_offer_selection(topup_data["plan"])
    final_balance = inital_balance - total_offer_price_with_comission
    log.info(f"final_balance:{final_balance}")
    submission = Submission(driver)
    final_wallet_balace=submission.submission_page("Your order is being processed.", "Unable to Process",
                               f"Reports\\{topup_data["plan"]}_sucess.png",
                               f"Reports\\{topup_data["plan"]}_failure.png")
    log.info(f"final_wallet_balace:{final_wallet_balace}")
    assert final_balance == final_wallet_balace

@pytest.mark.regression
@pytest.mark.parametrize("Addon_data", addon_Ons)
def test_Add_Ons_addsusbription(invoke_browser, Addon_data):
    driver = invoke_browser
    loginpage = Login(driver)
    loginpage.login(Addon_data["username"], Addon_data["password"])
    homepage = Homepage(driver)
    inital_balance=homepage.punchin_number(Addon_data["msisdn"])  #intial wallet balance
    homepage.find_Add_ons_menus()
    offerselection = OfferSelection(driver)
    total_offer_price_with_comission=offerselection.add_On_selection(Addon_data["plan"])  #offer price - commision
    final_balance = inital_balance - total_offer_price_with_comission
    print(final_balance)
    submission = Submission(driver)
    final_wallet_balance=submission.submission_page("Your order is being processed.", "Unable to Process",
                               f"Reports\\{Addon_data["plan"]}_sucess.png",
                               f"Reports\\{Addon_data["plan"]}_failure.png") #final wallet balance
    print(final_balance)
    assert final_balance == final_wallet_balance