from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_btn = (By.ID, "add_btn")
    __first_row = (By.XPATH, "//div[@id='row1']/input")
    __first_row_save_btn = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __second_row = (By.XPATH, "//div[@id='row2']/input")
    __second_row_save_btn = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __confirmation_msg = (By.ID, "confirmation")
    __edit_btn = (By.ID, "edit_btn")
    __instructions = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def click_edit_button(self):
        super()._click(self.__edit_btn)

    def is_second_row_displayed(self) -> bool:
        return super()._is_displayed(self.__second_row)

    def add_second_row(self, text:Optional[str]=None):
        super()._click(self.__add_btn)
        if text is not None:
            super()._type(self.__second_row, text)
            super()._click(self.__second_row_save_btn)
            super()._wait_until_element_is_visible(self.__confirmation_msg)

    def edit_first_row(self, text: str):
        super()._click(self.__edit_btn)
        super()._clear(self.__first_row)
        super()._type(self.__first_row, text)
        super()._click(self.__first_row_save_btn)
        super()._wait_until_element_is_visible(self.__confirmation_msg)

    @property
    def confirmation_msg(self) -> str:
        return super()._get_text(self.__confirmation_msg)

    def is_instruction_msg_invisible(self) -> bool:
        return super()._is_invisible(self.__instructions)
