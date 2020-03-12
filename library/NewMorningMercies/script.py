#!/usr/bin/python

import os

def getAllDays():
    pass

if __name__ == '__main__':
    # years = "2001"
    # years = int(years)
    # # 通过判断闰年，获取一年的总天数
    # days_sum = isLeapYear(years)
    for i in range(1,32):
        name = '03' + '%02d' % i + '.md'
        open(name, 'w')
    # 获取一年的所有日期
    #all_date_list = getAllDays("2000")
    #print(all_date_list)
