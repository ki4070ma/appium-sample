#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.account.accounts import Accounts
from page.common.basepage import BasePage

from appium import webdriver

class ThreeLineMenu(BasePage):

    def gnucash_label(self) -> Accounts:
        self._gnucash_label().click()
        return Accounts(self.driver)

    def favorites(self) -> Accounts:
        for el in self._menu_elements():
            if "Favorites" == el.text:
                el.click()
                return Accounts(self.driver, "FAVORITES")

    def _gnucash_label(self) -> webdriver:
        return self.driver.find_element_by_id('drawer_title')

    def _menu_elements(self) -> webdriver:
        return self.driver.find_elements_by_id('design_menu_item_text')
