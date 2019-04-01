#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any

from page.account.date_picker import DatePicker
from page.common.basepage import BasePage

from appium import webdriver


class NewTransactionPage(BasePage):

    def __init__(self, driver: webdriver, from_subsub_account: str) -> None:
        super(NewTransactionPage, self).__init__(driver)
        self.from_subsub_account = from_subsub_account

    def save(self) -> Any:  # TODO
        self._save().click()
        from page.account.subsub_accounts import SubSubAccountsPage
        return SubSubAccountsPage(self.driver, self.from_subsub_account)

    def input_description(self, desc: str) -> None:
        self._desc().send_keys(desc)

    def input_amount(self, val: int) -> None:
        self._amount().send_keys(val)

    def set_income_transaction_type(self) -> None:
        el = self._transaction_type()
        if "Charge" in el.text:
            el.click()

    def set_date(self, year: str, month: str, day: str) -> None:
        self._date().click()
        DatePicker(self.driver).set_date(year, month, day)

    def get_title(self) -> str:
        # FIXME temporary solution, top text on view is title for now
        return self._texts()[0].text

    def get_transaction_type(self) -> str:
        return self._transaction_type().text

    def _texts(self) -> webdriver:
        return self.driver.find_elements_by_class_name(
            'android.widget.TextView')

    def _desc(self) -> webdriver:
        return self.driver.find_element_by_id('input_transaction_name')

    def _amount(self) -> webdriver:
        return self.driver.find_element_by_id('input_transaction_amount')

    def _transaction_type(self) -> webdriver:
        return self.driver.find_element_by_id('input_transaction_type')

    def _save(self) -> webdriver:
        return self.driver.find_element_by_id('menu_save')

    def _date(self) -> webdriver:
        return self.driver.find_element_by_id('input_date')
