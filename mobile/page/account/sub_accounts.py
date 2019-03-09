#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.account.account_base import AccountBasePage
from page.account.subsub_accounts import SubSubAccountsPage
from page.common.utils import scroll_and_search_item

# e.g. Income


class SubAccountsPage(AccountBasePage):

    def __init__(self, driver, title):
        super(AccountBasePage, self).__init__(driver)
        self.title = title

    def account(self, label):
        scroll_and_search_item(self.driver, label).click()
        return SubSubAccountsPage(self.driver, ':'.join([self.title, label]))

    def get_title(self):
        # FIXME temporary solution, top text on view is title for now
        return self._text()[0].text

    def _text(self):
        return self.driver.find_elements_by_id('android:id/text1')
