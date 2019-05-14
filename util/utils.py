#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by imoyao at 2019/5/14 14:16
import time


def show_time(func):
    def wrap_func(*args, **kwargs):
        start_time = time.time()
        ret_result = func(*args, **kwargs)
        end_time = time.time()
        print('The function **{0}** takes {1} time.'.format(func.__name__, end_time - start_time))
        return ret_result

    return wrap_func


@show_time
def foo(n):
    for _ in list(range(n)):
        pass


if __name__ == '__main__':

    foo(100)
