# 随机生成字符串

import random
import string
from openpyxl import Workbook
from icecream import ic

def genrate_unique_string(length=10):
    '''
    生成10位唯一字符串
    :param length:
    :return:
    '''
    characters = string.ascii_letters + string.digits
    unique_string = ''.join(random.sample(characters, length))
    return unique_string

def main():
    '''
    创建一个新的excel工作表
    :return:
    '''
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'Unique String'

    # 写入excel
    for row in range(1, 3001):  # 生成3000个不重复的字符串
        unique_string = genrate_unique_string()
        sheet.cell(row=row, column=1, value=unique_string)

    wb.save("unique_strings.xlsx")
    ic("Unique strings saved to unique_strings.xlsx")

if __name__ == "__main__":
    main()