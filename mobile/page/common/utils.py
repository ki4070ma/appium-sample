#!/usr/bin/python
# -*- coding: utf-8 -*-


# FIXME Need better way to have global variable
class GlobalVar(object):

    log_root_dir = ''
    log_dir = ''

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


def get_window_size(driver):
    size = driver.get_window_size()
    return size['width'], size['height']


def scroll_and_search_item(driver, str):
    return driver.find_element_by_android_uiautomator(
        "new UiScrollable(new UiSelector().scrollable(true).instance(0))"
        ".scrollIntoView(new UiSelector().textContains(\"" +
        str +
        "\").instance(0))")
