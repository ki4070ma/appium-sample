#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.common.basepage import BasePage
from page.common.utils import get_window_size

from selenium.common.exceptions import NoSuchElementException


class DatePicker(BasePage):

    def __init__(self, driver):
        super(DatePicker, self).__init__(driver)
        self.w, self.h = get_window_size(self.driver)

    def set_date(self, year, month, day):
        self._set_year(year)
        date = ' '.join([day.zfill(2), month, year])
        # TODO Fix complicated logic
        if not (
            self._scroll_and_select_item(
                date,
                self._swipe_down,
                count=12) or self._scroll_and_select_item(
                date,
                self._swipe_update,
                count=24)):
            raise Exception("Couldn't find target date: " + date)
        self._save().click()

    def _set_year(self, year):
        el = self._year()
        if year != el.text:
            el.click()
            if eval(year) > eval(
                    el.text):  # target year > focused year => swipe up
                swipe = self._swipe_up
            else:  # target year < focused year => swipe down
                swipe = self._swipe_down
            self._scroll_and_select_item(year, swipe)

    def _scroll_and_select_item(self, str, swipe, count=100):
        for _ in range(count):
            swipe()
            try:
                self.driver.find_element_by_accessibility_id(str).click()
                return True
            except NoSuchElementException:
                pass
        return False

    def _year(self):
        return self.driver.find_element_by_id('date_picker_year')

    def _save(self):
        return self.driver.find_element_by_id('done_button')

    def _swipe_down(self):  # Only for date picker
        # TODO Should be robust
        self.driver.swipe(
            self.w / 2,
            self.h * 3 / 5,
            self.w / 5,
            self.h * 4 / 5)

    def _swipe_up(self):  # Only for date picker
        # TODO Should be robust
        self.driver.swipe(
            self.w / 5,
            self.h * 4 / 5,
            self.w / 2,
            self.h * 2.5 / 5)
