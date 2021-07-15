"""
功能描述：加载testData文件夹下所有的测试用例，并执行测试，生成测试报告，删除测试报告（两种删除方式）
编写人：SongXuwen
编写日期：
实现逻辑：
    1.加载所有的测试用例
        1.1 使用testLoader中的discover找到目标文件夹下所有的测试报告
            1.1.1 实例化testLoader
            1.1.2 调用discover的方式查找testCase下所有以test开头的文件中的测试用例，生成测试套件
    2.使用HTMLtestRunner执行测试报告
    3.清理测试报告
        3.1 清理所有的测试报告,每次全部清理
            3.1.1 获取报告所在的文件名
            3.1.2 获取报告文件夹下所有的文件名
            3.1.3 逐个清理报告，要使用路径加文件名清理
        3.2 清理旧的报告，只留最新的三份
            3.2.1 使用getctime获取报告的生成时间，组成时间列表，获取报告名列表
            3.2.2 将报告的生成时间和报告文件名列表分别取对应元素组成字典
            3.2.3 对时间列表进行排序，使用字典key值查出文件名的value值，循环删除至只剩余最新的两个报告


"""
import os
import time
import unittest
import HTMLTestRunner
import HwTestReport

from common.log import logger


def creat_suit():
    cur_dir = os.path.dirname(__file__)
    file_dir = cur_dir + '/testCase'
    suite = unittest.TestLoader().discover(start_dir=file_dir, pattern='test*.py')
    return suite


def clean_report():
    # 1.清理全部测试报告
    report_dir = os.path.dirname(__file__) + '/testReport/'
    report_list = os.listdir(report_dir)
    # for i in report_list:
    #     os.remove(report_dir + i)
    # logger.info('已清理全部测试报告------')

    # 2.清理旧测试报告，留最新的两份
    report_num = 2  # 删除后剩余的报告数量
    creat_time_list = [os.path.getctime(report_dir + i) for i in report_list]  # 生成报告的创建时间列表
    dict_report = {creat_time_list[i]: report_list[i] for i in range(len(report_list))}  # 将报告创建时间和报告名组成字段
    creat_time_list.sort()  #　将创建时间排序
    num = len(creat_time_list)-report_num  #　控制要删除的报告数量
    if len(report_list) <= report_num:
        #　判断存在的报告数量小于等于剩余的报告数量，无需删除报告
        logger.info('现在剩余报告数量为%s份，无需删除报告------' % len(report_list))
    else:
        for i in range(num):
            # 按照字典的key值-创建的时间，查找要删除的报告文件名，进行删除
            os.remove(report_dir + dict_report[creat_time_list[i]])
        logger.info('测试报告删除成功，剩余%d份最新报告------' % report_num)



def run_all():
    suite = creat_suit()
    # unittest.TextTestRunner().run(suite)
    report_dir = os.path.dirname(__file__) + '/testReport/'
    fp = report_dir + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()) + '-report.html'
    with open(fp, 'wb') as report:
        # runner = HTMLTestRunner.HTMLTestRunner(
        #     stream=report,
        #     title='UI test',
        #     description='发送微头条模块自动化测试用例执行情况'
        # )
        # runner.run(suite)
        # logger.info('执行测试用例完毕，生成测试报告--------------')
        runner = HwTestReport.HTMLTestReport(
            stream=report,
            title='UI test',
            description='发送微头条模块自动化测试用例执行情况',
            tester='SongXuwen'
        )
        runner.run(suite)
        logger.info('执行测试用例完毕，生成测试报告--------------')


if __name__ == '__main__':
    clean_report()
    run_all()
