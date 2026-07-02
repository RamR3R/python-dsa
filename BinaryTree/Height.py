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
node6 = TreeNode()
node6.val = 6
node7 = TreeNode()
node7.val = 7
node8 = TreeNode()
node8.val = 10
node9 = TreeNode()
node9.val = 9



root = node1
node1.left = node2
node1.right = node7
node2.left = node3
node2.right = node4
node4.left = node5
node4.right = node6
node7.left = node8
node7.right = node9



#to find the height of the BT

def dfs(root):
    #base condition
    if root == None:
        return 0
    
    leftHeight = dfs(root.left)
    rightHeight = dfs(root.right)

    return max(leftHeight , rightHeight) + 1
print(dfs(root))