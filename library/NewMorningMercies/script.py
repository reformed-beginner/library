#!/usr/bin/python

import os, sys

content = (
            u"---\n"
            u"layout: post\n"
            u"title: 晨恩日新 {0}\n"
            u"categories: NewMorningMercies\n"
            u"description: day {1}\n"
            u"keywords: 晨恩日新，保罗区普\n"
            u"comments: false\n"
            u"permalink: /library/NewMorningMercies/{2}\n"
            u"---\n"
            u"\n"
            u"## {0}\n"
            u"\n"
            u"### To <br> Do\n"
            u"\n"
            u"&emsp;&emsp;ToDo\n"
            u"\n"
            u"更多的信息和勉励：[]()\n"
          )

_MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七',u'十八', u'十九')
_P0 = (u'', u'十', u'百', u'千',)
_S4 = 10 ** 4

def _to_chinese4(num):
    assert (0 <= num and num < _S4)
    if num < 20:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num / 10
        lst.append(num)
        c = len(lst)  # 位数
        result = u''

        for idx, val in enumerate(lst):
            val = int(val)
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
                if idx < c - 1 and lst[idx + 1] == 0:
                    result += u'零'
        return result[::-1]

if __name__ == '__main__':
    month = 10
    for i in range(1,32):  # 31 or 32
        filename = '%02d' % month + '%02d' % i
        #print(filename)
        #os.system('cp ' + template + ' ' + name)
        date = _to_chinese4(month) + '月' + _to_chinese4(i) + '日'
        #print(date)
        filecontent = content.format(date, str(i), filename)
        with open(filename+'.md', 'w') as f:
            f.writelines(filecontent)

