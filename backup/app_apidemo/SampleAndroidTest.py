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
        # *** display density
        print(self.driver.get_display_density())

        # *** network status
        # from appium.webdriver.connectiontype import ConnectionType
        # print(self.driver.set_network_connection(ConnectionType.DATA_ONLY))

        # *** network speed
        # self.driver.set_network_speed('gsm')
        # self.driver.set_network_speed('evdo')
        # self.driver.set_network_speed('lte')
        # self.driver.set_network_speed('edge')
        # self.driver.set_network_speed('abc')

        # *** get_performance_data
        # print(self.driver.get_performance_data_types())
        # print(self.driver.get_performance_data("system_server", "cpuinfo", 10))

        # *** set_gsm_voice
        # 'unregistered', 'home', 'roaming', 'searching', 'denied', 'off', 'on'.
        # from appium.webdriver.extensions.gsm import GsmVoiceState
        # self.driver.set_gsm_voice(GsmVoiceState.OFF)
        # self.driver.set_gsm_voice(GsmVoiceState.ROAMING)

        # self.driver.set_gsm_voice(GsmVoiceState.ON)

        # *** set_power_capacity
        # self.driver.set_power_capacity(20)
        # from appium.webdriver.extensions.power import Power
        # self.driver.set_power_ac(Power.AC_OFF)
        # self.driver.set_power_ac('broken')

        # *** set_gsm_signal
        # self.driver.set_gsm_signal(100)
        # from appium.webdriver.extensions.gsm import GsmCallActions, GsmSignalStrength
        # self.driver.set_gsm_signal(GsmSignalStrength.GREAT)
        # self.driver.set_gsm_signal(GsmSignalStrength.POOR)
        # self.driver.set_gsm_signal(GsmSignalStrength.GOOD)

        # *** make_gsm_call
        # self.driver.make_gsm_call('09065532354', 'hoge')

        # *** get_system_bars
        # info = self.driver.get_system_bars()
        # print(info)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
