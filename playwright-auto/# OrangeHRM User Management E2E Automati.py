# OrangeHRM User Management E2E Automation (Python + Playwright)

##  Features
- Add, search, edit, validate, and delete users
- Page Object Model used
- One test case per file
- Smart selectors & waits

##  Setup


# 1. Clone this repository
git clone https://github.com/yourusername/orangehrm-e2e.git
cd orangehrm-e2e

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install
# Run all test cases
pytest tests/

# Run a specific test
pytest tests/test_add_user.py



## 🧑‍💻 Sample Code Snippets

### `pages/login_page.py`


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('button:has-text("Login")')

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_tab = page.locator('a:has-text("Admin")')
        self.add_button = page.locator('button:has-text("Add")')
        self.search_input = page.locator('input[placeholder="Search"]')
        self.search_button = page.locator('button:has-text("Search")')
        self.save_button = page.locator('button:has-text("Save")')

    def navigate_to_admin(self):
        self.admin_tab.click()

    def click_add_user(self):
        self.add_button.click()

    # Add methods like `fill_user_form`, `edit_user`, `delete_user`...
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

    # Fill the form and save - implement this in admin page
    # admin.fill_user_form(...)

    assert page.locator('div:has-text("Success")').is_visible()



