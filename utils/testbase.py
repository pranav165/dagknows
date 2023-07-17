# We will add fixtures here that can be reused across tests
from pages.login import LoginPage
from config.config import Config
from utils.driverclass import DriverClass


class TestBase:

    def open_login_page(self,init_driver):
        page_obj = init_driver
        url = Config.app_url
        page_obj.open(url)
        return page_obj
