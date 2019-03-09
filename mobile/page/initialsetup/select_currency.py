#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.initialsetup.account_setup import AccountSetup
from page.initialsetup.initialsetup_base import InitialSetupBase


class SelectCurrency(InitialSetupBase):

    def next(self):
        super(SelectCurrency, self).next()
        return AccountSetup(self.driver)
