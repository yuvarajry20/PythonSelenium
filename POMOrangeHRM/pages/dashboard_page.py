from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    dashboard_heading = (By.XPATH, "//h6[text()='Dashboard']")
    assign_leave_option = (By.XPATH, "//p[text()='Assign Leave']")
    time_at_work_section = (By.XPATH, "//p[text()='Time at Work']")

    def get_dashboard_heading(self):
        return self.get_text(self.dashboard_heading)

    def get_assign_leave_text(self):
        return self.get_text(self.assign_leave_option)

    def get_time_at_work_text(self):
        return self.get_text(self.time_at_work_section)
