#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.initialsetup.feedback_options import FeedbackOptions
from page.initialsetup.initialsetup_base import InitialSetupBase


class AccountSetup(InitialSetupBase):

    def next(self) -> FeedbackOptions:
        super(AccountSetup, self).next()
        return FeedbackOptions(self.driver)
