# OrangeHRM User Management E2E Automation

## Manual Test Cases

1. **Navigate to Admin Module**
   - Login as Admin
   - Click on the 'Admin' tab
   - Verify Admin page loads

2. **Add a New User**
   - Go to Admin module
   - Click 'Add' button
   - Fill user details (role, status, employee name, username, password)
   - Click 'Save'
   - Verify success message

3. **Search the Newly Created User**
   - Go to Admin module
   - Enter username in search
   - Click 'Search'
   - Verify user appears in results

4. **Edit all Possible User Details**
   - Search for the user
   - Click 'Edit'
   - Change details (role, status, etc.)
   - Click 'Save'
   - Verify success message

5. **Validate Updated Details**
   - Search for the user
   - Verify updated details are shown

6. **Delete the User**
   - Search for the user
   - Select and click 'Delete'
   - Confirm deletion
   - Verify user is removed

---

## Automation Steps

1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   playwright install
   ```
2. Run all tests:
   ```powershell
   pytest tests/
   ```
3. Run a specific test:
   ```powershell
   pytest tests/test_add_user.py
   ```

## Playwright Version
- Please specify the version in your requirements.txt (e.g., `playwright==1.44.0`)

## Project Structure
```
/pages
  login_page.py
  admin_page.py
/tests
  test_navigate_admin.py
  test_add_user.py
  test_search_user.py
  test_edit_user.py
  test_validate_user.py
  test_delete_user.py
README.md
requirements.txt
```

---

## Sample Page Object (login_page.py)
```python
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('button:has-text("Login")')

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
```

---

## Sample Test (test_add_user.py)
```python
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
```

---

## How to Push to GitHub
1. Initialize git:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/Akshun10/orangehrm-e2e.git
   git push -u origin main
   ```

---

Replace `YourUsername` with your GitHub username. Update the code and selectors as needed for your application.
