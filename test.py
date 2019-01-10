#!/usr/bin/python

import os
import unittest

from appium import webdriver

def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

caps = {
    'platformName': "Android",
    'platformVersion': "8.0",
    'deviceName': "Android",
    'appPackage': "com.google.android.music",
    'appActivity': ".tv.HomeActivity",
    'app': PATH("./playmusic.apk"),
    'automationName': "uiautomator2"
}


class BaseTest(unittest.TestCase):
    def __init__(self, methodName):
        super(BaseTest, self).__init__(methodName)
        self.caps = caps

    def setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.caps)

    def tearDown(self):
        # end the session
        self.driver.quit()


class TmpTest(BaseTest):

    def test_test(self):

        import time
        time.sleep(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TmpTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
