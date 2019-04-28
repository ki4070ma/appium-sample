#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import unittest

from appium import webdriver


def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android',
        'app': PATH(app),
        'automationName': 'uiautomator2'
    }

    return desired_caps


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', get_desired_capabilities('ApiDemos-debug.apk'))

    def tearDown(self):
        self.driver.quit()

    def test_01_test_name(self):
        self.driver.toggle_airplane_mode()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
