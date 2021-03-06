import unittest

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

# https://discuss.leetcode.com/topic/85778/dfs-c-python-solutions
# by @zqfan


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = [0]
        def dfs(n, p):
            if n is None:
                return 0, 0
            li, ld = dfs(n.left, n)
            ri, rd = dfs(n.right, n)
            longest[0] = max(longest[0], li + rd + 1, ld + ri + 1)
            if n.val == p.val + 1:
                return max(li, ri) + 1, 0
            if n.val == p.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0
        dfs(root, root)
        return longest[0]


class Test(unittest.TestCase):

    def test(self):
        case = tree_deserialize('[1,2,3]')
        assert Solution().longestConsecutive(case) == 2
        case = tree_deserialize(
            '[1,2,3,4,10,null,null,5,null,null,9,6,null,null,8]')
        assert Solution().longestConsecutive(case) == 3
        case = '[-1,-2,null,-3,null,-4]'
        case = tree_deserialize(case)
        assert Solution().longestConsecutive(case) == 4

        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main()
