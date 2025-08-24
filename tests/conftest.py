import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver= None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome, firefox, Edge"
    )



@pytest.fixture(scope="function")
def invoke_browser(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    browser_name=request.config.getoption("--browser_name")
    if browser_name =="chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://domo-eload-uat.m1.com.sg/login")
        time.sleep(3)
    elif browser_name =="firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://domo-eload-uat.m1.com.sg/login")
        time.sleep(3)
    elif browser_name =="Edge":
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.get("https://domo-eload-uat.m1.com.sg/login")
        time.sleep(3)
    yield driver
    driver.close()



@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                relative_path = os.path.relpath(file_name, start=os.path.dirname(item.config.option.htmlpath))
                html = f'<div><img src="{relative_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append( pytest_html.extras.html( html ) )
        report.extra = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)