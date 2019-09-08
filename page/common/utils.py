#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Tuple, Any

from appium import webdriver

# FIXME Need better way to have global variable


class GlobalVar(object):

    log_root_dir = ''
    log_dir = ''

    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:  # TODO
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


def get_window_size(driver: webdriver) -> Tuple[int, int]:
    size = driver.get_window_size()
    return size['width'], size['height']


def scroll_and_search_item(driver: webdriver, word: str) -> webdriver:
    return driver.find_element_by_android_uiautomator(
        "new UiScrollable(new UiSelector().scrollable(true).instance(0))"
        ".scrollIntoView(new UiSelector().textContains(\"" +
        word +
        "\").instance(0))")
