#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import unittest


from page.account.accounts import Accounts
from page.initialsetup.welcome import Welcome
from page.common.utils import get_window_size, GlobalVar

from appium import webdriver


# Returns abs path relative to this file and not cwd
def PATH(p: str) -> str: return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


caps = {
    'platformName': "Android",
    'platformVersion': "8.0",
    # 'platformVersion': "9",
    'deviceName': "Android Emulator",
    'appPackage': "org.gnucash.android",
    'appActivity': ".ui.account.AccountsActivity",
    'app': PATH('./gnucash.apk'),
    'automationName': "uiautomator2",
}


class BaseTest(unittest.TestCase):
    def __init__(self, method_name: str) -> None:
        super(BaseTest, self).__init__(method_name)
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


class SampleAndroidTest(BaseTest):

    def testtest(self) -> None:

        # print(self.driver.location)
        # print(self.driver.finger_print(1))

        print('*****')

#        self.driver.send_sms("090-6553-2354", "Hello")

        self.driver.toggle_airplane_mode()

        # print(self.driver.get_settings())
        # data = {'waitForIdleTimeout': 10001}
        # self.driver.update_settings(data)
        # print(self.driver.get_settings())
        # data = {'waitForIdleTimeout': 10000}
        # self.driver.update_settings(data)
        # print(self.driver.get_settings())

        import time
        time.sleep(3)


if __name__ == '__main__':
    import datetime as dt
    GlobalVar().log_root_dir = os.path.join(PATH('.'), 'output', dt.datetime.now().strftime('%y%m%d-%H%M%S'))
    os.path.isdir(GlobalVar().log_root_dir) or os.makedirs(GlobalVar().log_root_dir)

    suite = unittest.TestLoader().loadTestsFromTestCase(SampleAndroidTest)  # For debug
    unittest.TextTestRunner(verbosity=2).run(suite)
