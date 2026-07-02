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

def dfs(root , arr):
    if root == None or arr[0] == 0:
        return
    
    dfs(root.left , arr)
    arr[0] -= 1

    if arr[0] == 0:
        arr[1] = root.val
    dfs(root.right , arr)


    



arr = [5 , 3, 4 , 2 , 1, 6]
root = TreeNode()
root.val = arr[0]
for i in range( 1 , len(arr)):
    insert(root , arr[i])

k = int(input())
res = [k , -1]
dfs(root , res)
print(res[1])

