#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Tuple

from page.account.whats_new_dialog import WhatsNewDialog
from page.initialsetup.initialsetup_base import InitialSetupBase

from appium import webdriver


class Review(InitialSetupBase):

    def done(self) -> WhatsNewDialog:
        super(Review, self).next()
        return WhatsNewDialog(self.driver)

    def get_list(self) -> List[Tuple[str, str]]:
        return [(el_key.text, el_val.text)
                for el_key, el_val in zip(self._keys(), self._vals())]

    def _keys(self) -> webdriver:
        return self.driver.find_elements_by_id('text1')

    def _vals(self) -> webdriver:
        return self.driver.find_elements_by_id('text2')
