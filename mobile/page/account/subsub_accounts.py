#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.account.account_base import AccountBasePage

# e.g. Income:Salary


class SubSubAccountsPage(AccountBasePage):

    def __init__(self, driver, title):
        super(AccountBasePage, self).__init__(driver)
        self.title = title

    def new_transaction(self):
        self._new_transaction_btn().click()
        from page.account.new_transaction import NewTransactionPage
        return NewTransactionPage(self.driver, self.title)

    def get_title(self):
        return self._texts()[0].text

    def get_position_new_transaction_btn(self):
        pos = self._create_transaction().location
        return pos['x'], pos['y']

    def _create_transaction(self):
        return self.driver.find_element_by_id('fab_create_transaction')

    def _texts(self):
        return self.driver.find_elements_by_id('android:id/text1')

    def _new_transaction_btn(self):
        return self.driver.find_element_by_id('fab_create_transaction')
