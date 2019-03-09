#!/usr/bin/python
# -*- coding: utf-8 -*-

from page.initialsetup.initialsetup_base import InitialSetupBase
from page.initialsetup.review import Review


class FeedbackOptions(InitialSetupBase):

    def next(self):
        super(FeedbackOptions, self).next()
        return Review(self.driver)
