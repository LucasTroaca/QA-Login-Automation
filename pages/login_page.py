class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.submit_button = page.locator("#submit")

    def go_to(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()