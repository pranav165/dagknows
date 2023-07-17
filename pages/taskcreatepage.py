from utils.pagebase import PageBase


class CreateTaskPage(PageBase):
    task_title = "xpath@@//input[@class='search_powered_textbox_field']"
    task_description = "xpath@@//*[@data-placeholder='Description']"
    task_type_select = "xpath@@//select[@class='custom-select script_type_dropdown']"
    task_tag = "xpath@@//*[@class='tag_input']"
    task_cmd = "xpath@@//*[@class='cm-line']"
    save = "xpath@@//button[text()='Save']"

    def __init__(self, selenium_driver=None):
        PageBase.__init__(self, selenium_driver)
        self.wait_for_page_to_load()

    def create_runbook(self, runbook_data):
        """
        Click on create runbook
        """
        self.wait_till_element_is_present(self.task_title)
        self.send_keys(self.task_title, runbook_data["task_title"])
        self.send_keys(self.task_description, runbook_data["task_description"])
        self.select_dropdown_option(self.task_type_select, runbook_data["task_type"])
        self.sleep_in_seconds(2)
        self.send_keys(self.task_cmd,runbook_data["task_cmd"])
        self.send_keys(self.task_tag, runbook_data["task_tag"])
        self.click(self.save)
        return self
