import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_second_row_displayed(), "Second row is unexpectedly not displayed"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row("Shawerma")
        assert exceptions_page.confirmation_msg == "Row 2 was saved", "Confirmation message is not as expected."


    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.edit_first_row("Shawerma")
        assert exceptions_page.confirmation_msg == "Row 1 was saved", "Confirmation message is not as expected"

    @pytest.mark.debug
    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_instruction_msg_invisible(), "Instruction text is unexpectedly still visible."
