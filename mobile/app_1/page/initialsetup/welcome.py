#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.initialsetup.default_currency import DefaultCurrency
from page.initialsetup.initialsetup_base import InitialSetupBase


class Welcome(InitialSetupBase):

    def next(self) -> DefaultCurrency:
        super(Welcome, self).next()
        return DefaultCurrency(self.driver)
