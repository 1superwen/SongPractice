"""
功能描述：输出日志到控制态的模块
编写人：SongXuwen
编写日期：
实现逻辑：
    1.导包，logging
    2.日志的基础设置。logging.basicCongif()
        2.1 设置日志级别level，设置日志输出信息format={}
    3.设置日志输出文件名，logging.getLog
    4.返回单例logger(),方便调用

"""
import logging
def log():
    logging.basicConfig(level=logging.INFO, format='%(name)s'
                                                    '-[level:%(levelname)s]'
                                                    '-[%(asctime)s]'
                                                    '-[File:%(filename)s]'
                                                    '-[line:%(lineno)d]'
                                                    '-[Msg:%(message)s]')

    logger = logging.getLogger('UI_Test_Log')
    return logger

logger = log()


if __name__ == '__main__':
    logger = log()
    logger.info('hahaha')
    logger.debug('hahaha')