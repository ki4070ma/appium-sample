#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.account.date_picker import DatePicker
from page.common.basepage import BasePage


class NewTransactionPage(BasePage):

    def __init__(self, driver, from_subsub_account):
        super(NewTransactionPage, self).__init__(driver)
        self.from_subsub_account = from_subsub_account

    def save(self):
        self._save().click()
        from page.account.subsub_accounts import SubSubAccountsPage
        return SubSubAccountsPage(self.driver, self.from_subsub_account)

    def input_description(self, desc):
        self._desc().send_keys(desc)

    def input_amount(self, val):
        self._amount().send_keys(val)

    def set_income_transaction_type(self):
        el = self._transaction_type()
        if "Charge" in el.text:
            el.click()

    def set_date(self, year, month, day):
        self._date().click()
        DatePicker(self.driver).set_date(year, month, day)

    def get_title(self):
        # FIXME temporary solution, top text on view is title for now
        return self._texts()[0].text

    def get_transaction_type(self):
        return self._transaction_type().text

    def _texts(self):
        return self.driver.find_elements_by_class_name(
            'android.widget.TextView')

    def _desc(self):
        return self.driver.find_element_by_id('input_transaction_name')

    def _amount(self):
        return self.driver.find_element_by_id('input_transaction_amount')

    def _transaction_type(self):
        return self.driver.find_element_by_id('input_transaction_type')

    def _save(self):
        return self.driver.find_element_by_id('menu_save')

    def _date(self):
        return self.driver.find_element_by_id('input_date')
