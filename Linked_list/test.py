#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by imoyao at 2019/9/23 17:50


# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# from functools import wraps
#
#
# def singleton(cls):
#     _instance = {}
#
#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kwargs)
#         return _instance[cls]
#
#     return wrapper
#
#
# @singleton
# class A:
#     pass
#
#
# a = A()
# b = A()
# print(a is b)
# class Singleton:
#     _instance = None

#     def __new__(cls,*args,**kwargs):
#         if not cls._instance:
#             cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
#         return cls._instance

# a = Singleton()
# b = Singleton()

# print(a is b)
