from utils.pagebase import PageBase
from pages.homepage import HomePage

class LoginPage(PageBase):
    sign_in = "xpath@@//*[@href='/vlogin']"
    username = "email"
    password = "password"
    sign_in_submit = "xpath@@//*[@value='Sign in']"

    def __init__(self, selenium_driver=None):
        PageBase.__init__(self, selenium_driver)
        self.wait_for_page_to_load()

    def login(self,username,password):
        """
        Navigate to options from the left panel
        """
        self.click(self.sign_in)
        self.wait_till_element_is_present(self.username)
        self.send_keys(self.username,username)
        self.send_keys(self.password, password)
        self.sleep_in_seconds(5)
        self.javascript_click(self.sign_in_submit)
        self.sleep_in_seconds(10)
        return self.becomes(HomePage)

    def is_user_logged_in(self):
        if self.is_element_displayed(self.sign_in):
            return False
        return True

