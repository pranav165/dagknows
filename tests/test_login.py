from utils.testbase import TestBase
from config.config import Config


class TestLogin(TestBase):
    driver = None

    def test_login_valid_creds(self, login):
        """
        Test for login with valid credentials
        """
        login_page = login
        assert login_page.assert_logged_in() is True

    def test_login_invalid_password(self, open_login_page):
        """
        Test for login with invalid password
        """
        login_page = open_login_page
        login_page.login(username=Config.email, password="!@#!@$")
        assert login_page.is_show_Error("Invalid credential.") is True
        assert login_page.is_login_screen() is True

    def test_login_invalid_username(self, open_login_page):
        """
        Test for login with invalid username
        """
        login_page = open_login_page
        login_page.login(username="testEmail", password=Config.password)
        assert login_page.is_login_screen() is True

    def test_login_invalid_username_password(self, open_login_page):
        """
        Test for login with invalid username and password
        """
        login_page = open_login_page
        login_page.login(username="testEmail", password="123")
        assert login_page.is_login_screen() is True

    def test_login_blank(self, open_login_page):
        """
        Test for login with blank username and password
        """
        login_page = open_login_page
        login_page.login(username="", password="")
        assert login_page.is_login_screen() is True

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
