#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by imoyao at 2019/10/28 18:15

# https://blog.csdn.net/xinxin957_/article/details/81915443
# https://blog.csdn.net/zzfightingy/article/details/86742755
class Node:
    """
    定义Node类，用于表示树上的节点
    """

    def __init__(self, data, left_tree=None, right_tree=None):
        """
        节点值、左子树、右子树
        :param data:
        :param left_tree:
        :param right_tree:
        """
        self.data = data
        self.left_subtree = left_tree
        self.right_subtree = right_tree


class BinTree:
    """
    定义二叉树类
    """

    def __init__(self, root=None):
        self.root = root

    def add_node(self, val):
        """
        添加元素
        :param val:
        :return:
        """
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                current = queue.pop(0)  # 从列表头部拿元素
                if current.left_subtree is None:
                    current.left_subtree = new_node
                    return
                elif current.right_subtree is None:
                    current.right_subtree = new_node
                    return
                else:
                    queue.append(current.left_subtree)
                    queue.append(current.right_subtree)

    def bfs_travel(self):
        """
        广度优先遍历
        :return:
        """
        if self.root is None:
            return
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                current = queue.pop(0)
                print(current.data, end=' ')
                if current.left_subtree is not None:
                    queue.append(current.left_subtree)
                if current.right_subtree is not None:
                    queue.append(current.right_subtree)

    def dfs_travel_preorder(self, node):
        """
        深度优先前序遍历（递归实现）
        :param node:
        :return:
        """
        if node is None:
            return
        else:
            print(node.data, end=' ')
            self.dfs_travel_preorder(node.left_subtree)
            self.dfs_travel_preorder(node.right_subtree)

    def dfs_travel_inorder(self, node):
        """
        深度优先中序遍历（递归实现）
        :param node:
        :return:
        """
        if node is None:
            return
        else:
            self.dfs_travel_inorder(node.left_subtree)
            print(node.data, end=' ')
            self.dfs_travel_inorder(node.right_subtree)

    def dfs_travel_postorder(self, node):
        """
        深度优先后序遍历（递归实现）
        :param node:
        :return:
        """
        if node is None:
            return
        else:
            self.dfs_travel_postorder(node.left_subtree)
            self.dfs_travel_postorder(node.right_subtree)
            print(node.data, end=' ')


if __name__ == '__main__':
    t = BinTree()
    for i in range(10):
        t.add_node(1)
    t.bfs_travel()
    print('bfs_travel')
    t.dfs_travel_preorder()
