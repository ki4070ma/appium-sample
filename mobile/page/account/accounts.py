#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Tuple

from page.account.account_base import AccountBasePage
from page.common.utils import scroll_and_search_item

from appium import webdriver

class Accounts(AccountBasePage):

    def __init__(self, driver: webdriver, tab='ALL') -> None:
        super(AccountBasePage, self).__init__(driver)
        self.tab = tab

    def account(self, label: str):  # TODO
        from page.account.sub_accounts import SubAccountsPage
        scroll_and_search_item(self.driver, label).click()
        return SubAccountsPage(self.driver, label)

    def favorite_icon(self, label: str) -> None:
        self._favorite_icons()[self.get_labels().index(label)].click()

    def get_title(self) -> str:
        # FIXME temporary solution, top text on view is title for now
        return self._texts()[0].text

    def get_position_create_btn(self) -> Tuple[float, float]:
        pos = self._create_btn().location
        return pos['x'], pos['y']

    def is_tab_focused(self, tab: str) -> bool:
        ret = False
        for el in self._tabs():
            if tab == el.text and el.is_selected:
                ret = True
                break
        return ret

    def _create_btn(self) -> webdriver:
        return self.driver.find_element_by_id('fab_create_account')

    def _favorite_icons(self) -> webdriver:
        return self.driver.find_elements_by_id('favorite_status')

    def _tabs(self) -> webdriver:
        return self.driver.find_elements_by_class_name(
            'android.widget.TextView')

    def _texts(self) -> webdriver:
        return self.driver.find_elements_by_class_name(
            'android.widget.TextView')
