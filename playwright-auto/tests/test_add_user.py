import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")
    admin.navigate_to_admin()
    admin.click_add_user()
    # admin.fill_user_form(...)
    assert page.locator('div:has-text("Success")').is_visible()
