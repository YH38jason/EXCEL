# coding=utf-8
import xlrd
path = ''
while path != 'q':
    try:
        path = input('输入要读取的工作簿：')
        book = xlrd.open_workbook(path)
        sheet = book.sheet_by_name(input('要打开的工作表：'))
        for j in range(sheet.nrows):
            rowString = ''
            r = sheet.row(j)
            for i in r:
                rowString = rowString + str(i.value) + '\t'
            print(rowString)
    except FileNotFoundError:
        print('文件未找到：')
    except xlrd.XLRDError:
            print('读取错误！')
