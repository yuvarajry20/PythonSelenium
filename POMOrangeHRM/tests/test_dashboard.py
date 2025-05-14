import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestOrangeHRMDashboard:
    def test_dashboard_heading(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        dashboard_page = DashboardPage(self.driver)
        heading = dashboard_page.get_dashboard_heading()
        assert heading == "Dashboard", f"Expected 'Dashboard', but got '{heading}'"

    def test_assign_leave_text(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        dashboard_page = DashboardPage(self.driver)
        assign_leave_text = dashboard_page.get_assign_leave_text()
        assert assign_leave_text == "Assign Leave", f"Expected 'Assign Leave', but got '{assign_leave_text}'"

    def test_time_at_work_text(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        dashboard_page = DashboardPage(self.driver)
        time_at_work_text = dashboard_page.get_time_at_work_text()
        assert time_at_work_text == "Time at Work", f"Expected 'Time at Work', but got '{time_at_work_text}'"