# Definition for a binary tree node.
from collections import deque
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        r = root
        queue = deque()
        lvl = 1
        queue.append((r, lvl))
        lvl_sum = defaultdict(lambda: 0)

        while(queue):
            r, lvl = queue.pop()
            lvl_sum[lvl] += r.val
            if r.right != None:
                queue.append((r.right, lvl+1))
            if r.left != None:
                queue.append((r.left, lvl+1))

        return max(lvl_sum.keys(), key=(lambda k: lvl_sum[k]))
