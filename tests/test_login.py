from pages.login_page import LoginPage
from data.login_data import login_test_data
import pytest


@pytest.mark.parametrize ("username, password, expected", login_test_data)
def test_login(login_page, username, password, expected):
    login_page.login(username, password)
    expected(login_page)