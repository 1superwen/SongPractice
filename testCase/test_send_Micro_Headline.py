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
    3.断言操作后页面是否和预期一致(找到刚发布的微头条是否在页面元素中)
"""
import unittest
# 直接导入已经实例好的driver
from selenium.webdriver.common.by import By

from common.driver import driver


class Test_SendCase(unittest.TestCase):


    def test_send_Micro_Headline(self):
        # 2.定位和操作
        # 2.1.定位：定位到发布按钮，操作，点击发布
        driver.find_element(By.ID,'com.ss.android.article.news:id/bpw').click()
        # 2.2.定位：定位到微头条，操作：点击微头条
        driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        # 2.3定位：定位到输入框，操作：输入测试的文本
        test_wb = '发布一条微头条_1'
        driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys(test_wb)
        # 2.4定位：定位到发布按钮，操作：点击发布
        driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
        # self.assertIn()断言发送后的结果
        self.assertIn(test_wb+'s', driver.page_source), f'未找到{test_wb}，发布微头条失败'

if __name__ == '__main__':
    # s = Test_SendCase()
    # s.send_Micro_Headline()
    unittest.main()
