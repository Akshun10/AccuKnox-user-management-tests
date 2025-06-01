import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_navigate_admin(page):
    login = LoginPage(page)
    admin = AdminPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")
    admin.navigate_to_admin()
    assert page.locator('h6:has-text("Admin")').is_visible()
