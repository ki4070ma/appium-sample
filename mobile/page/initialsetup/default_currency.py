#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.initialsetup.account_setup import AccountSetup
from page.initialsetup.initialsetup_base import InitialSetupBase
from page.initialsetup.select_currency import SelectCurrency
from page.common.utils import scroll_and_search_item


class DefaultCurrency(InitialSetupBase):

    def __init__(self, driver):
        super(InitialSetupBase, self).__init__(driver)
        self.select_currency_flg = False

    def next(self):
        super(DefaultCurrency, self).next()
        return SelectCurrency(
            self.driver) if self.select_currency_flg else AccountSetup(
            self.driver)

    def scroll_and_select_item(self, currency):
        el = scroll_and_search_item(self.driver, currency)
        if el.text == u"Other…":
            self.select_currency_flg = True
        el.click()
