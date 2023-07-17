import os
import pytest
from datetime import datetime
from utils.driverclass import DriverClass
from pages.login import LoginPage
from config.config import Config
from utils.driverclass import driverlist


def get_project_root():
    # returns root project directory to build paths for other functions
    path = os.path.join(os.path.dirname(__file__))
    return os.path.abspath(path)


screenshot_path = os.path.join(get_project_root(), "reports", "screenshots")


@pytest.fixture(scope="function", autouse=True)
def init_driver():
    driver = DriverClass.register_driver()
    page_obj = LoginPage(driver)
    yield page_obj
    driver.quit()


@pytest.fixture(scope="function", autouse=False)
def open_login_page(init_driver):
    login_page = init_driver
    url = Config.app_url
    login_page.open(url)
    return login_page


@pytest.fixture(scope="function", autouse=False)
def login(init_driver):
    page_obj = init_driver
    url = Config.app_url
    page_obj.open(url)
    homepage = page_obj.login(Config.email, Config.password)
    return homepage


@pytest.fixture(scope="function", autouse=False)
def login_blank(init_driver):
    page_obj = init_driver
    url = Config.app_url
    page_obj.open(url)
    homepage = page_obj.login("", "")
    return homepage

#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     try:
#         driver = driverlist[0]
#         timestamp = datetime.now().strftime('%H-%M-%S')
#
#         pytest_html = item.config.pluginmanager.getplugin('html')
#         outcome = yield
#         report = outcome.get_result()
#         extra = getattr(report, 'extra', [])
#         if report.when == "call" or report.when == "setup" or report.when == "teardown":
#             try:
#
#                 # always add url to report
#                 xfail = hasattr(report, 'wasxfail')
#                 if (report.skipped and xfail) or (report.failed and not xfail):
#                     driver.save_screenshot(screenshot_path + timestamp + '.png')
#                     # only add additional html on failure
#                     img_src = os.path.abspath(
#                         os.path.join(get_project_root(), "reports", screenshot_path + timestamp + '.png'))
#                     extra.append(pytest_html.extras.image(img_src))
#                     extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#             except:
#                 print("error")
#         report.extra = extra
#     except:
#         print("error")
