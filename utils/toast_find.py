#!/usr/bin/env python
# encoding:UTF-8
# @Author  : SUN FEIFEI

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_toast(driver, text, timeout=30, poll_frequency=0.5):
    """is toast exist, return True or False"""
    # noinspection PyBroadException
    try:
        toast = ("xpath", ".//*[contains(@text,'%s')]" % text)
        WebDriverWait(driver, timeout, poll_frequency)\
            .until(EC.presence_of_element_located(toast))
        return True
    except Exception:
        return False
