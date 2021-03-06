import bisect
import collections
import cProfile
import heapq
import itertools
import math
import re
import unittest
from pprint import pprint

import numpy as np

'''

'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def tree_deserialize(string):
    """
    author: @StefanPochmann
    """
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def tree_height(root):
    """
    author: @StefanPochmann
    """
    return 1 + max(tree_height(root.left), tree_height(root.right)) if root else -1


def tree_draw(root):
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = tree_height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """
        self.d = collections.defaultdict(list)
        def pre_order(node):
            if node.left:
                self.d[node.val].append(node.left.val)
                self.d[node.left.val].append(node.val)
                pre_order(node.left)

            if node.right:
                self.d[node.val].append(node.right.val)
                self.d[node.right.val].append(node.val)
                pre_order(node.right)
        pre_order(root)

        def k_distance(s, k):
            new = [s]
            seen = set(new)
            if k == 0:
                return new
            for i in range(k):
                new = [nn for n in new for nn in self.d[n] if nn not in seen]
                seen = seen.union(new)
            return new

        return k_distance(target.val, K)


class Test(unittest.TestCase):

    def test(self):
        cases = [
            [dict(root = tree_deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), target = 5, K = 1), set([7,4,1])]
        ]
        for ci, co in cases:
            tmp = set(Solution().distanceK(**ci))
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
