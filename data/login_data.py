from pages.login_page import LoginPage

login_test_data = [
    ("student", "Password123", LoginPage.expect_login_success),
    ("incorrect_user", "Password123", LoginPage.expect_invalid_user),
    ("student", "incorrectPassword", LoginPage.expect_invalid_password),
    ("incorrect_user", "incorrectPassword", LoginPage.expect_invalid_user),
    ("", "Password123", LoginPage.expect_invalid_user),
    ("student", "", LoginPage.expect_invalid_password),
    ("", "", LoginPage.expect_invalid_user),
]