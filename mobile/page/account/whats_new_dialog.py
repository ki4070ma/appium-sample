#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.account.accounts import Accounts
from page.common.basepage import BasePage


class WhatsNewDialog(BasePage):

    def dismiss(self):
        self._dismiss().click()
        return Accounts(self.driver, "ALL")

    def get_title(self):
        return self._title().text

    def _title(self):
        return self.driver.find_element_by_id('android:id/alertTitle')

    def _dismiss(self):
        return self.driver.find_element_by_id('android:id/button1')
