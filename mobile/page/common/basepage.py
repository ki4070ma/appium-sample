#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from page.common.utils import GlobalVar

from appium import webdriver

class BasePage(object):
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        # FIXME temporary solution, to wait window transition finished
        self._wait_transition()

        import datetime as dt
        img_path = os.path.join(GlobalVar().log_dir, dt.datetime.now().strftime('%y%m%d-%H%M%S') + '.png')
        self.driver.get_screenshot_as_file(img_path)

    def _wait_transition(self) -> None:
        import time
        # time.sleep(10)  # For low performance device (e.g. emulator on low
        # spec pc)
        time.sleep(3)
