class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None

node1 = TreeNode()
node1.val = 1
node2 = TreeNode()
node2.val = 2
node3 = TreeNode()
node3.val = 3
node4 = TreeNode()
node4.val = 4
node5 = TreeNode()
node5.val = 5


root = node1
root.left = node2
root.right = node3

root.left.left = node4
root.left.right = node5



#BFS
from collections import deque
q = deque()
q.append(root)
while len(q) > 0 :
    x = q.popleft()
    print(x.val)
    if x.left != None:
        q.append(x.left)
    if x.right != None:
        q.append(x.right)