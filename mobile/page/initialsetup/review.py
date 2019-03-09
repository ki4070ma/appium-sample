#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.account.whats_new_dialog import WhatsNewDialog
from page.initialsetup.initialsetup_base import InitialSetupBase


class Review(InitialSetupBase):

    def done(self):
        super(Review, self).next()
        return WhatsNewDialog(self.driver)

    def get_list(self):
        return [(el_key.text, el_val.text)
                for el_key, el_val in zip(self._keys(), self._vals())]

    def _keys(self):
        return self.driver.find_elements_by_id('text1')

    def _vals(self):
        return self.driver.find_elements_by_id('text2')
