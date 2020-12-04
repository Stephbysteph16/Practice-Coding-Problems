from collections import defaultdict
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root: TreeNode):
    
    r = root
    queue = deque()
    lvl = 1
    queue.append((r,lvl))
    lvl_sum = defaultdict(lambda:0)
    
    while(queue):
        r, lvl = queue.pop()
        lvl_sum[lvl] += r.val
        if r.right != None:
            queue.append((r.right, lvl+1))
        if r.left != None:
            queue.append((r.left,lvl+1))
    
    
    return max(lvl_sum.keys(), key=(lambda k: lvl_sum[k]))
        
        


if __name__ == '__main__':
    print(maxLevelSum([1, 7, 0, 7, -8, None, None]))
        
