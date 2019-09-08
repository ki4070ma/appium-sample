#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.account.accounts import Accounts
from page.common.basepage import BasePage

from appium import webdriver


class WhatsNewDialog(BasePage):

    def dismiss(self) -> Accounts:
        self._dismiss().click()
        return Accounts(self.driver, "ALL")

    def get_title(self) -> str:
        return self._title().text

    def _title(self) -> webdriver:
        return self.driver.find_element_by_id('android:id/alertTitle')

    def _dismiss(self) -> webdriver:
        return self.driver.find_element_by_id('android:id/button1')
