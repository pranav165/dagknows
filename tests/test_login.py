from utils.testbase import TestBase
from config.config import Config


class TestLogin(TestBase):
    driver = None

    def test_login_valid_creds(self, login):
        """
        Test for login with valid credentials
        """
        login_page = login
        login_page.assert_logged_in()

    def test_login_invalid_password(self,init_driver):
        """
        Test for login with invalid password
        """
        login_page = init_driver
        login_page.login(username=Config.email, password="!@#!@$")
        assert login_page.is_user_logged_in() is False

    def test_login_blank(self, login):
        """
        Test for login
        """
        login_page = self.login_user(self.driver)
        login_page.assert_logged_in()

    def test_create_runbook(self, login):
        runbook_data = {
            "task_title": "test_runbook",
            "task_description": "test description for runbook",
            "task_type": "Commands",
            "task_tag": "automation",
            "task_cmd": "ls"

        }

        login_page = login
        login_page.select_create_runbook() \
            .create_runbook(runbook_data)

    def test_search_runbook(self, login):
        login_page = login
        assert login_page.search_for_runbook("test_runbook").is_runbook_exists("test_runbook")
