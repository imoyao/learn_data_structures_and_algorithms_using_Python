#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by imoyao at 2019/5/15 11:04
"""
字典操作及性能测试
"""
import pathlib
import sys
import timeit

util_p = pathlib.Path('../..').resolve()
sys.path.append(str(util_p))
from util import utils


