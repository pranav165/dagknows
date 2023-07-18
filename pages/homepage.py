from utils.pagebase import PageBase
from pages.taskcreatepage import CreateTaskPage


class HomePage(PageBase):
    create_runbook = "xpath@@//button[contains(@class,'create-runbook')]"
    user_menu = "xpath@@//div[@id='user_icon_container']"
    search_runbook = "xpath@@//input[@placeholder='Search for runbooks']"
    runbook = "xpath@@//a[contains(@href,'tasks')]"

    def __init__(self, selenium_driver=None):
        PageBase.__init__(self, selenium_driver)
        self.wait_for_page_to_load()

    def assert_logged_in(self):
        return self.is_element_displayed(self.user_menu)

    def select_create_runbook(self):
        """
        Click on create runbook
        """
        self.wait_till_element_is_present(self.create_runbook)
        self.sleep_in_seconds(30)
        self.javascript_click(self.create_runbook)
        return self.becomes(CreateTaskPage)

    def search_for_runbook(self,name):
        """
        Search for a runbook by name
        """
        self.sleep_in_seconds(30)
        self.send_keys(self.search_runbook,name)
        self.sleep_in_seconds(5)
        self.hit_enter(self.search_runbook)
        self.sleep_in_seconds(5)
        return self

    def is_runbook_exists(self,name):
        self.wait_for_page_to_load()
        runbooks = self.find_elements(self.runbook)
        for runbook in runbooks:
            if runbook.text == name:
                print("Found runbook in the search results")
                return True
        return False

