"""
功能描述：实现读取目标excel的数据的模块开发
编写人：SongXuwen
编写日期：2021-6-15
实现逻辑：
    1.找到目标excel文件的位置
    2.导入xlrd模块
    3.使用文件的位置打开对应的excel文件
    4.选择对应的工作表sheet
    5.逐行读取工作表中的数据
        前提规划：创建空列表，将每行的数据以一个字典的形式存储在列表中，字典的key值分别为第一行的数据，value值为第二行开始每一行对应的数据
        5.1 先求出工作表的最大行数
        5.2 读取工作表的第一行，作为key值
        5.3 使用for循环，从第2行开始循环读取文件到最大的行数，得到的值作为value值
        5.4 将key和value组成字典，可以使用字典推导式，将整个字典追加到列表中
        5.5 return 列表，方便一调用这个方法就可以获得列表数据

"""
# 导入需要的模块
import xlrd, os

#　定义readExcel类,使用大驼峰，与模块区分开
class ReadExcel():
    # 将读取excel中相关的属性初始化一下
    def __init__(self):
        # 1.找到目标excel文件的位置,使用os.path.dirname找到最上级的文件路径。拼接上excel文件所在位置
        self.excel = os.path.dirname(os.path.dirname(__file__)) + r'\testData\data.xls'
        # 2.导入xlrd模块
        # 3.使用文件的位置打开对应的excel文件
        self.readbook = xlrd.open_workbook(self.excel)
        # 4.选择对应的工作表sheet
        self.sheet = self.readbook.sheet_by_name('sheet1')
        # 5.1先求出工作表的最大行数
        self.row = self.sheet.nrows

    #定义读取方法，来进行读取文件操作
    def read(self):
        # 5.逐行读取工作表中的数据
        # 前提规划：创建空列表，将每行的数据以一个字典的形式存储在列表中，字典的key值分别为第一行的数据，value值为第二行开始每一行对应的数据
        data = []

        # 5.1先求出工作表的最大行数
        # 5.2读取工作表的第一行，作为key值
        key_list = self.sheet.row_values(0)

        # 5.3使用for循环，从第2行开始循环读取文件到最大的行数，得到的值作为value值
        for i in range(1, self.row):
            value_list = self.sheet.row_values(i)
            # 5.4将key和value组成字典，可以使用字典推导式，将整个字典追加到列表中
            dict1 = {key_list[j]: value_list[j] for j in range(0, len(key_list))}
            data.append(dict1)
        # 5.5turn 列表，方便一调用这个方法就可以获得列表数据
        return data

a = ReadExcel()
print(a.read())