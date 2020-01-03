#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest

from page.common.utils import get_window_size, GlobalVar

from appium import webdriver

# Returns abs path relative to this file and not cwd


def PATH(p: str) -> str: return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


caps = {
    'platformName': "Android",
    'deviceName': "Android Emulator",
    'appPackage': "org.gnucash.android",
    'appActivity': ".ui.account.AccountsActivity",
    'app': PATH('../gnucash.apk'),
    'newCommandTimeout': 240,
    'automationName': 'UIAutomator2',
    'uiautomator2ServerInstallTimeout': 120000,
    'adbExecTimeout': 120000,
    'androidInstallTimeout': 120000
}


class BaseTestCase(unittest.TestCase):
    def __init__(self, method_name: str) -> None:
        super(BaseTestCase, self).__init__(method_name)
        self.caps = caps

    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.caps)
        self.width, self.height = get_window_size(self.driver)

        # Start taking evidence
        self.make_log_dir(self._testMethodName)
        self.driver.start_recording_screen()

    def tearDown(self) -> None:
        # Stop taking evidence
        img_path = os.path.join(os.getcwd(), self._testMethodName + '.png')
        self.driver.get_screenshot_as_file(img_path)

        payload = self.driver.stop_recording_screen()
        with open(os.path.join(GlobalVar().log_dir, "cap.mp4"), "wb") as fd:
            import base64
            fd.write(base64.b64decode(payload))

        with open(os.path.join(GlobalVar().log_dir, "log.txt"), "w") as fd:
            logs = self.driver.get_log('logcat')
            for lines in logs:
                for line in lines['message'].split('¥n'):
                    fd.write(line + '\n')

        # end the session
        self.driver.quit()

    @staticmethod
    def make_log_dir(dir_name: str) -> None:
        GlobalVar().log_dir = os.path.join(GlobalVar().log_root_dir, dir_name)
        os.path.isdir(GlobalVar().log_dir) or os.makedirs(GlobalVar().log_dir)


def is_ci():
    """Returns if current execution is running on CI
    Returns:
        bool: `True` if current executions is on CI
    """
    return os.getenv('CI', 'false') == 'true'
