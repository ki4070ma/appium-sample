#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.common.basepage import BasePage


class AccountBasePage(BasePage):

    def three_line_menu(self):
        self._three_line_menu().click()
        from page.account.three_line_menu import ThreeLineMenu
        return ThreeLineMenu(self.driver)

    def get_labels(self):
        return [el.text for el in self._labels()]

    def get_balance(self, label):
        index = [el.text for el in self._labels()].index(label)
        return [el.text for el in self._balances()][index]

    def get_position_three_line_menu(self):
        pos = self._three_line_menu().location
        return pos['x'], pos['y']

    def _three_line_menu(self):
        return self.driver.find_element_by_accessibility_id(
            'Navigation drawer opened')

    def _labels(self):
        return self.driver.find_elements_by_id('primary_text')

    def _balances(self):
        return self.driver.find_elements_by_id('account_balance')
