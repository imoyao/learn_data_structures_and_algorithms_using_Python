#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by imoyao at 2019/5/13 18:33


def binary_search(sorted_lists, wanted_item):
    low_index = 0
    high_index = len(sorted_lists) - 1
    count = 0
    while low_index <= high_index:
        count += 1
        mid_index = (low_index + high_index) // 2
        # print(mid_index)
        mid_item = sorted_lists[mid_index]
        if mid_item == wanted_item:
            print('It takes {0} times to find {1} in index {2}'.format(count, wanted_item, mid_index))
            return mid_item
        else:
            if mid_item < wanted_item:
                low_index = mid_index + 1
            else:
                high_index = mid_index - 1
    return None


if __name__ == '__main__':
    a = binary_search(list(range(100)), 50)
    print('ret:', a)
