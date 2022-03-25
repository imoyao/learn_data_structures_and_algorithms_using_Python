#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@create: 2022/3/25 17:55
@file: leetcode707.py
@author: imoyao
@email: immoyao@gmail.com
@desc:
"""
'''
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    # def __repr__(self):
    #     return self.val


class NodeList:

    def __init__(self):
        self.size = 0
        self.head = Node(0)

    def __iter__(self):
        current = self.head
        while current.next is not None:
            yield current.val
            current = current.next

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.val

    def add_at_index(self, index, val):
        if index > self.size:
            return None
        if index < 0:
            index = 0

        self.size += 1
        # 找到被放置节点的前一个，在哪里放置，就for几次
        prev = self.head  # 基准节点
        for _ in range(index):
            prev = prev.next
        # 构造被插入节点
        add_node = Node(val)
        add_node.next = prev.next
        # 放入断链位置
        prev.next = add_node

    def add_at_head(self, val):
        self.add_at_index(0, val)

    def add_at_tail(self, val):
        self.add_at_index(self.size, val)

    def delete_at_index(self, index):
        if index < 0 or index > self.size:
            return None
        self.size -= 1
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
if __name__ == '__main__':


    nl = NodeList()
    for item in range(10):
        if item % 2 == 0:
            nl.add_at_head(item)
        else:
            nl.add_at_tail(item)

    for item in nl:
        print(item)
