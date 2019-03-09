#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.account.accounts import Accounts
from page.common.basepage import BasePage


class ThreeLineMenu(BasePage):

    def gnucash_label(self):
        self._gnucash_label().click()
        return Accounts(self.driver)

    def favorites(self):
        for el in self._menu_elements():
            if "Favorites" == el.text:
                el.click()
                return Accounts(self.driver, "FAVORITES")

    def _gnucash_label(self):
        return self.driver.find_element_by_id('drawer_title')

    def _menu_elements(self):
        return self.driver.find_elements_by_id('design_menu_item_text')
