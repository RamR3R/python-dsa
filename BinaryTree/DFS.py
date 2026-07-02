class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None


def dfs(root):
    #base condition
    if root == None:
        return
    
    #inorder travesal
    dfs(root.left)
    print(root.val)
    dfs(root.right)

    #pre order traversal
    print(root.val)
    dfs(root.left)
    dfs(root.right)

    #post orerTraversal
    dfs(root.left)
    dfs(root.right)
    print(root.val)


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


dfs(root)