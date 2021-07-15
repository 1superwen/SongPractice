"""
功能描述：获取启动app的driver
编写人：SongXuwen
编写日期：
实现逻辑：
    1.导包
    2.设置启动参数
    3.启动app获取到driver
    4.返回driver

"""
from appium import webdriver
import time

from common.log import logger


class Driver():
    def __init__(self):
        self.desire_caps = {
            'deviceName': '127.0.0.1:21503',
            'platformName': 'Android',
            'platformVersion': '5.1.1',
            'appPackage': 'com.ss.android.article.news',
            'appActivity': 'com.ss.android.article.news.activity.MainActivity',
            'noReset': True,
            'unicodeKeyboard': True,
        }

    def setUp(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desire_caps)
        logger.info('driver启动中-------')
        time.sleep(5)
        return driver
d = Driver()
driver = d.setUp()

if __name__ == '__main__':
    d = Driver()
    d.setUp()

