import pytest

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_msg",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_msg):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.is_error_msg_displayed(), "Error message is not displayed, but it should be"
        assert login_page.error_msg == expected_error_msg, "Error message is not as expected"
