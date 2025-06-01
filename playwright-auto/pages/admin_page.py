from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
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

    # Add methods like fill_user_form, edit_user, delete_user as needed
