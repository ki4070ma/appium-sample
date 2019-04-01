#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any

from page.common.basepage import BasePage
from page.common.utils import scroll_and_search_item

from appium import webdriver

class InitialSetupBase(BasePage):

    def next(self) -> Any:
        self._next().click()
        # return Next page

    def back(self) -> None:
        self._back().click()
        # return Back page

    def get_title(self) -> str:
        return self._title().text

    def scroll_and_select_item(self, name: str) -> None:
        scroll_and_search_item(self.driver, name).click()

    def _next(self) -> webdriver:
        return self.driver.find_element_by_id('btn_save')

    def _back(self) -> webdriver:
        return self.driver.find_element_by_id('btn_xxx')

    def _title(self) -> webdriver:
        return self.driver.find_element_by_id("android:id/title")
