"""
功能描述：将测试结果写入Excel文件中
编写人：SongXuwen
编写日期：
实现逻辑：
    0.导包，xlrd打开文件，xlutils.copy复制文件
    1.使用xlrd打开要写入的文件，创建打开文件对象rb rb = xlrd.open_workbook(dir)
    2.复制文件cb，使用copy cb = copy(rb)
    3.确定要写入文件的工作表 sheet = cb.get_sheet(0)
    4.写入数据  sheet.write(x,y,value)
    5.保存文件  cb.save(dir)


"""
import xlrd, os
from xlutils.copy import copy


class WriteExcel():
    def __init__(self):
        self.file_dir = os.path.dirname(os.path.dirname(__file__)) + '/testData/data.xls'
        self.rb = xlrd.open_workbook(self.file_dir)
        self.cb = copy(self.rb)
        self.sh = self.cb.get_sheet(0)

    def writeexcel(self):
        self.sh.write(1, 6, '实际结果')
        self.cb.save(os.path.dirname(os.path.dirname(__file__)) + '/testData/data1.xls')

if __name__ == '__main__':
    r = WriteExcel()
    r.writeexcel()
