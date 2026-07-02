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
    print(root.val , end=" ")
    dfs(root.right)

def delete(root , val):
    if val > root.val:
        root.right = delete(root.right , val)
    elif val < root.val:
        root.left = delete(root.left , val)
    else:
        if root.left == None and root.right == None:
            return None
        elif root.left == None:
            return  root.right
        elif root.right == None:
            return root.left

        else:# there 2 children for my node
            #find the successor.
            successor = root.right
            while successor.left != None:
                successor = successor.left
            #succus found....
            root.val = successor.val
            root.right = delete(root.right , successor.val)
    return root


arr = [50 , 70 , 30 , 20 , 40 , 60 , 80]
root = TreeNode()
root.val = arr[0]
for i in range( 1 , len(arr)):
    insert(root , arr[i])

x = int(input())
dfs(root)
delete(root , x)
dfs(root)