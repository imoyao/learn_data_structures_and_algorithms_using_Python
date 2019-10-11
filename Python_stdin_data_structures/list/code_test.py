#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by imoyao at 2019/5/15 11:04
"""
列表操作及性能测试
"""

import timeit

from util import utils


@utils.show_time
def list_plus(n):
    a_list = []
    for i in range(n):
        a_list += [i]
    return a_list


@utils.show_time
def list_append(n):
    a_list = []
    for i in range(n):
        a_list.append(i)
    return a_list


@utils.show_time
def list_expression(n):
    return [_ for _ in range(n)]


# @utils.show_time
def list_range(n):
    return list(range(n))


if __name__ == '__main__':
    # t1 = timeit.Timer('list_plus(1000)', 'from __main__ import list_plus', )
    # print(f'{list_plus.__name__} takes {t1.timeit(number=1000)} ms.')
    #
    # t2 = timeit.Timer('list_append(1000)', 'from __main__ import list_append')
    # print(f'{list_append.__name__} takes {t1.timeit(number=1000)} ms.')
    #
    # t3 = timeit.Timer('list_expression(1000)', 'from __main__ import list_expression')
    # print(f'{list_expression.__name__} takes {t1.timeit(number=1000)} ms.')
    #
    # t4 = timeit.Timer('list_range(1000)', 'from __main__ import list_range')
    # print(f'{list_range.__name__} takes {t1.timeit(number=1000)} ms.')

    # 上方为使用timeit模块的测试，下方为使用自写装饰器的测试

    n = 1000000
    list_plus(n)
    list_append(n)
    list_expression(n)
    list_range(n)
    '''
    # 输出
    The function **list_plus** takes 0.47864699363708496 time.
    The function **list_append** takes 0.41912221908569336 time.
    The function **list_expression** takes 0.14060020446777344 time.
    The function **list_range** takes 0.06196928024291992 time.
    '''

    # 两种不同方式pop()操作耗时对比

    n = 10000
    x = list_range(n)
    p1 = timeit.Timer('x.pop()', 'from __main__ import x')
    print(f'list_pop_normal takes {p1.timeit(number=1000)} ms.')

    p2 = timeit.Timer('x.pop(0)', 'from __main__ import x')
    print(f'list_pop_index takes {p2.timeit(number=1000)} ms.')
    '''
    对比两次，发现指定index时耗时会随着list的增大而增加
    n = 1000000
    list_pop_normal takes 0.0006615779711864889 ms.
    list_pop_index takes 1.150215208006557 ms.  
    # n = 10000
    list_pop_normal takes 0.00041822699131444097 ms.
    list_pop_index takes 0.0079622509656474 ms.
    '''
