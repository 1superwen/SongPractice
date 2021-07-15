"""
功能描述：连接手机启动app
编写人：SongXuwen
编写日期：
实现逻辑：
    1.
    2.
    3.

"""

from appium import webdriver
import os, time

def starup():
    print('---启动中')
    desire_caps = {
        'deviceName': '127.0.0.1:21503',
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'appPackage': 'com.ss.android.article.news',
        'appActivity': '.activity.MainActivity',
        'noReset': True,
        'unicodeKeyboard': True,
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
    print('启动完成，等待1秒')
    time.sleep(1)
    return driver
    # login_button = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[4]/android.widget.TabWidget/android.widget.RelativeLayout[5]')
    # login_button.click()
    # login_2 = driver.find_element_by_id('com.ss.android.article.news:id/cje')
    # login_2.click()
    #
    # driver.close_app()


if __name__ == '__main__':
    starup()