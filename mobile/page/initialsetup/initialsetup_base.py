#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.common.basepage import BasePage
from page.common.utils import scroll_and_search_item


class InitialSetupBase(BasePage):

    def next(self):
        self._next().click()
        # return Next page

    def back(self):
        self._back().click()
        # return Back page

    def get_title(self):
        return self._title().text

    def scroll_and_select_item(self, name):
        scroll_and_search_item(self.driver, name).click()

    def _next(self):
        return self.driver.find_element_by_id('btn_save')

    def _back(self):
        return self.driver.find_element_by_id('btn_xxx')

    def _title(self):
        return self.driver.find_element_by_id("android:id/title")
