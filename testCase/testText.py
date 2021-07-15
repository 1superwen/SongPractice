"""
功能描述：
编写人：SongXuwen
编写日期：
实现逻辑：
    1.
    2.
    3.

"""
import time

from selenium.webdriver.common.by import By

from AppiumPratice.appium_test1 import starup

def testtext():
        driver = starup()
        # a = driver.find_elements(By.CLASS_NAME, 'android.view.View')[0].get_attribute("content-desc")
        # print(a)
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="关注"]').click()
        a = driver.find_elements(By.ID, 'com.ss.android.article.news:id/aee')[1].get_attribute("name")
        print(a)
        time.sleep(5)
if __name__ == '__main__':
    testtext()