class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None

def insert(root , val):
    if root == None:
        newNode = TreeNode()
        newNode.val = val
        return newNode  

    if val > root.val:
        root.right = insert(root.right , val)
    else:
        root.left = insert(root.left , val)

    return root


def dfs(root):
    if root == None:
        return
    dfs(root.left)
    print(root.val)
    dfs(root.right)

arr = [50 , 70 , 30 , 20 , 40 , 60 , 80]
root = TreeNode()
root.val = arr[0]
for i in range( 1 , len(arr)):
    insert(root , arr[i])
dfs(root)
