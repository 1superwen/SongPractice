"""
功能描述：创建MyTest基类，较少重复代码
编写人：SongXuwen
编写日期：
实现逻辑：
    1.导包
    2.继承unittest.TestCase
    3.定以重复使用的方法

"""

import unittest
from common.driver import Driver
from common.log import logger

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Driver().startUp()
    def setUp(self) -> None:
        self.driver.launch_app()
        logger.info('重新启动app------')

    def tearDown(self) -> None:
        self.driver.close_app()
        logger.info('关闭app------')
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        logger.info('退出进程------')

