from playwright.sync_api import expect
class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.submit_button = page.locator("#submit")
        self.error = page.locator("#error")
        self.logout = page.locator(".wp-block-button__link")
        self.titulo = page.locator(".post-title")
        self.username_error = "Your username is invalid!"
        self.password_error = "Your password is invalid!"
        self.success_url = "https://practicetestautomation.com/logged-in-successfully/"

    def go_to(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()

    def expect_login_success(self):
        expect(self.page).to_have_url(self.success_url)
        expect(self.titulo).to_be_visible()
        expect(self.logout).to_be_visible()

    def expect_invalid_user(self):
        expect(self.error).to_be_visible()
        expect(self.error).to_have_text(self.username_error)
        self.page.screenshot(path="screenshots/invalid_username.png")

    def expect_invalid_password(self):
        expect(self.error).to_be_visible()
        expect(self.error).to_have_text(self.password_error)
        self.page.screenshot(path="screenshots/invalid_password.png")

    def expect_no_username(self):
        expect(self.error).to_be_visible()
        expect(self.error).to_have_text(self.username_error)
        self.page.screenshot(path="screenshots/no_username.png")

    def expect_no_password(self):
        expect(self.error).to_be_visible()
        expect(self.error).to_have_text(self.password_error)
        self.page.screenshot(path="screenshots/no_password.png")

    def expect_no_credentials(self):
        expect(self.error).to_be_visible()
        expect(self.error).to_have_text(self.username_error)
        self.page.screenshot(path="screenshots/no_credentials.png")