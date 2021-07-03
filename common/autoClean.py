"""
功能描述：自动清理无顺序测试报告
编写人：SongXuwen
编写日期：
实现逻辑：
    自动清理测试报告
        1.获取目标文件下的所有文件列表
            os.path.listdir()
        2.判断当前文件下的报告数量是否超过三个 if len(list_file) >3
            2.1 超过三个
                2.1.1 遍历目标文件下每个文件的创建时间os.path.getctime，组成一个时间列表
                        ctime_list = [j for j in list(dir + '/' + i): os.path.getctime(dir + '/' + i)]
                2.1.2 使用字典推导式，将文件列表和时间列表组成字典
                        dict = {ctime[i]: file_list[i]  for i in range(len(ctime_list)}
                2.1.3 将时间列表进行排序
                        new_ctime_list = ctime_list.sort()
                2.1.4 获取旧的时间列表
                        old_ctime_list = [i for i in range(-3, 0)]
                2.1.5 遍历删除旧的文件
                        for i in old_ctime_list():
                            os.path.remove(dir+'/'+dict[i])

"""
import os
def auto_clear(num=3):
    """
    自动清理过期测试报告
    :param num: 剩余最新的报告数量
    :return:
    """

    file_dir = os.path.dirname(__file__) + r'/testReport/'
    # 1.os.listdir()，接收生成的文件名列表
    # file_list = os.listdir(file_dir)
    # if len(file_list) > 2:
    #     for i in file_list[:-2]:
    #         os.remove(file_dir + i)
    file_list = os.listdir(file_dir)
    if len(file_list) > num:
        ctime_list = [os.path.getctime(file_dir + '/' + i) for i in file_list]
        file_dict = {ctime_list[i]: file_list[i] for i in range(len(ctime_list))}
        new_ctime_list = sorted(ctime_list)
        remove_ctime_list = new_ctime_list[:-num]
        for i in remove_ctime_list:
            os.remove(file_dir + '/' + file_dict[i])
        # logger.info('已清理过期测试报告')
        print('已清理过期测试报告')