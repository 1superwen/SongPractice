"""
功能描述：发送微头条的测试用例
编写人：SongXuwen
编写日期：
实现逻辑：
    1.打开app，获取到driver前置条件：账号已登陆
    2.定位和操作
        2.1.定位：定位到发布按钮，操作，点击发布
        2.2.定位：定位到微头条，操作：点击微头条
        2.3定位：定位到输入框，操作：输入测试的文本
        2.4定位：定位到发布按钮，操作：点击发布
    3.断言操作后页面是否和预期一致
"""
import time
import unittest
from selenium.webdriver.common.by import By

from common.log import logger
from common.myTest import MyTest
from common.readExcel import ReadExcel

r = ReadExcel()


class SendMicroHeadline(MyTest):
    # @unittest.skip
    def test1_normal_len(self):
        # 2.定位和操作
        # 2.1.定位：定位到发布按钮，操作，点击发布
        logger.info('发送正常长度微头条用例------')
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bpw').click()
        # 2.2.定位：定位到微头条，操作：点击微头条
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        # 2.3定位：定位到输入框，操作：输入测试的文本
        # 获取类名和方法名
        classname = self.__class__.__name__
        methodname = self._testMethodName
        test_wb = r.get_data(classname, methodname)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys(test_wb)
        time.sleep(3)
        # 2.4定位：定位到发布按钮，操作：点击发布
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
        time.sleep(3)
        # self.assertIn()断言发送后的结果
        real = self.driver.find_elements(By.ID, 'com.ss.android.article.news:id/aee')[0].get_attribute("name")
        self.assertIn(test_wb, real), f'未找到{test_wb}，发布微头条失败'


    # @unittest.skip
    def test2_max_len(self):
        # 2.定位和操作
        # 2.1.定位：定位到发布按钮，操作，点击发布
        logger.info('发送最长长度微头条用例------')
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bpw').click()
        # 2.2.定位：定位到微头条，操作：点击微头条
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        # 2.3定位：定位到输入框，操作：输入测试的文本
        # 获取类名和方法名
        classname = self.__class__.__name__
        methodname = self._testMethodName
        test_wb = r.get_data(classname, methodname)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys(test_wb)
        time.sleep(3)
        # 2.4定位：定位到发布按钮，操作：点击发布
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
        time.sleep(3)
        # self.assertIn()断言发送后的结果、
        real = self.driver.find_elements(By.ID, 'com.ss.android.article.news:id/aee')[0].get_attribute("name")
        self.assertIn(test_wb, real), f'未找到{test_wb}，发布微头条失败'


    # @unittest.skip
    def test3_min_len(self):
        # 2.定位和操作
        # 2.1.定位：定位到发布按钮，操作，点击发布
        logger.info('发送最短长度微头条用例------')
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bpw').click()
        # 2.2.定位：定位到微头条，操作：点击微头条
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        # 2.3定位：定位到输入框，操作：输入测试的文本
        # 获取类名和方法名
        classname = self.__class__.__name__
        methodname = self._testMethodName
        test_wb = r.get_data(classname, methodname)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys(test_wb)
        time.sleep(3)
        # 2.4定位：定位到发布按钮，操作：点击发布
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
        time.sleep(3)
        # self.assertIn()断言发送后的结果
        real = self.driver.find_elements(By.ID, 'com.ss.android.article.news:id/aee')[0].get_attribute("name")
        self.assertIn(test_wb, real), f'未找到{test_wb}，发布微头条失败'

    @unittest.skip
    def test4_symbols_len(self):
        # 2.定位和操作
        # 2.1.定位：定位到发布按钮，操作，点击发布
        logger.info('发送符号组成微头条用例------')
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bpw').click()
        # 2.2.定位：定位到微头条，操作：点击微头条
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        # 2.3定位：定位到输入框，操作：输入测试的文本
        # 获取类名和方法名
        classname = self.__class__.__name__
        methodname = self._testMethodName
        test_wb = r.get_data(classname, methodname)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys(test_wb)
        time.sleep(3)
        # 2.4定位：定位到发布按钮，操作：点击发布
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
        time.sleep(3)
        # self.assertIn()断言发送后的结果
        real = self.driver.find_elements(By.ID, 'com.ss.android.article.news:id/aee')[0].get_attribute("name")
        self.assertIn(test_wb, real), f'未找到{test_wb}，发布微头条失败'    # @unittest.skip

    # @unittest.skip
    def test5_small_message_len(self):
        # 2.定位和操作
        # 2.1.定位：定位到发布按钮，操作，点击发布
        logger.info('发送英文字母微头条用例------')
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bpw').click()
        # 2.2.定位：定位到微头条，操作：点击微头条
        self.driver.find_element(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        # 2.3定位：定位到输入框，操作：输入测试的文本
        # 获取类名和方法名
        classname = self.__class__.__name__
        methodname = self._testMethodName
        test_wb = r.get_data(classname, methodname)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys(test_wb)
        time.sleep(3)
        # 2.4定位：定位到发布按钮，操作：点击发布
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
        time.sleep(3)
        # self.assertIn()断言发送后的结果
        real = self.driver.find_elements(By.ID, 'com.ss.android.article.news:id/aee')[0].get_attribute("name")
        self.assertIn(test_wb, real), f'未找到{test_wb}，发布微头条失败'


if __name__ == '__main__':
    unittest.main(verbosity=2)
