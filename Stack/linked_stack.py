#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by imoyao at 2019/9/17 15:58

"""
基于链表实现的栈
"""


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self._next = next


class LinkedStack:
    """A stack based upon singly-linked list.
    """

    def __init__(self):
        self._top = None
        self._size = 0

    def __repr__(self):
        current = self._top
        nums = []
        while current:
            nums.append(current.data)
            current = current._next
        ret = ','.join([str(num) for num in nums])
        return f'[{ret}]'

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def push(self, item):
        new_top = Node(item)
        new_top._next = self._top
        self._top = new_top
        self._size += 1

    def pop(self):
        if not self._size:
            print('Stack Overflow')
        else:
            item = self._top.data
            self._top = self._top._next
            return item

    def top(self):
        if not self._size:
            print('Stack Overflow.')
        else:
            return self._top.data


s = LinkedStack()
print(s.is_empty())
s.push(4)
print(s)
s.push('dog')
print(s)
# print(s.peek())
s.push(True)
print(s)
print(s.size())
print(s.is_empty())
print(s)

# class LinkedStack:
#     """
#     基于单链表的栈实现
#     """
#
#     def __init__(self):
#         self._top = None
#         self._num = 0
#
#     def is_empty(self):
#         return self._num == 0
#
#     def size(self):
#         return self._num
#
#     # def __repr__(self):
#     #     current = self._top
#     #     nums = []
#     #     while current:
#     #         nums.append(current._data)
#     #         current = current._next
#     #     return ' '.join(f'{num}' for num in nums)
#
#     def push(self, value):
#         new_top = Node(value)
#         new_top._next = self._top
#         self._top = new_top
#         self._num += 1
#
#     def pop(self):
#         if not self._num:
#             print('The length of stack is 0.')
#         else:
#             item = self._top._data
#             self._top = self._top.next
#             return item
#
#
# if __name__ == '__main__':
#     s = LinkedStack()
#     print(s.is_empty())
#     s.push(4)
#     print(s)
#     s.push('dog')
#     print(s)
#     # print(s.peek())
#     s.push(True)
#     print(s)
#     print(s.size())
#     print(s.is_empty())
#     print(s)
