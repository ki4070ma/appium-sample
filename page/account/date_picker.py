#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any

from page.common.basepage import BasePage
from page.common.utils import get_window_size

from selenium.common.exceptions import NoSuchElementException

from appium import webdriver


class DatePicker(BasePage):

    def __init__(self, driver: webdriver) -> None:
        super(DatePicker, self).__init__(driver)
        self.w, self.h = get_window_size(self.driver)

    def set_date(self, year: str, month: str, day: str) -> None:
        self._set_year(year)
        date = ' '.join([day.zfill(2), month, year])
        # TODO Fix complicated logic
        if not (
            self._scroll_and_select_item(
                date,
                self._swipe_down,
                count=12) or self._scroll_and_select_item(
                date,
                self._swipe_up,
                count=24)):
            raise Exception("Couldn't find target date: " + date)
        self._save().click()

    def _set_year(self, year: str) -> None:
        el = self._year()
        if year != el.text:
            el.click()
            if eval(year) > eval(
                    el.text):  # target year > focused year => swipe up
                swipe = self._swipe_up
            else:  # target year < focused year => swipe down
                swipe = self._swipe_down
            self._scroll_and_select_item(year, swipe)

    def _scroll_and_select_item(self, word: str, swipe: Any, count: int = 100) -> bool:  # TODO Any -> _swipe_down/up
        for _ in range(count):
            swipe()
            try:
                self.driver.find_element_by_accessibility_id(word).click()
                return True
            except NoSuchElementException:
                pass
        return False

    def _year(self) -> webdriver:
        return self.driver.find_element_by_id('date_picker_year')

    def _save(self) -> webdriver:
        return self.driver.find_element_by_id('done_button')

    def _swipe_down(self) -> None:  # Only for date picker
        # TODO Should be robust
        self.driver.swipe(
            self.w / 2,
            self.h * 3 / 5,
            self.w / 5,
            self.h * 4 / 5)

    def _swipe_up(self) -> None:  # Only for date picker
        # TODO Should be robust
        self.driver.swipe(
            self.w / 5,
            self.h * 4 / 5,
            self.w / 2,
            self.h * 2.5 / 5)
