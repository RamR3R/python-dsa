class Node:
    def __init__(self):
        self.val = 0
        self.next = None

#Linked List code
obj1 = Node()
obj1.val = 8
obj2 = Node()
obj2.val = 5
obj3 = Node()
obj3.val = 4
obj4 = Node()
obj4.val = 13
obj1.next = obj2
obj2.next = obj3
obj3.next = obj4

head = obj1


n = int(input("Enter new Node value : "))
newNode = Node()
newNode.val = n
position = int(input("Enter position to insert : "))

#insert at the head
# newNode.next = head
# head = newNode

#insert at the tail
# current = head
# while current.next != None:
#     current = current.next
# current.next = newNode


#insert at a position i
current = head
count = 1
while count < position - 1:
    current = current.next
    count += 1

newNode.next = current.next
current.next = newNode






#traversal
current = head
while current != None:
    print(current.val , end=" => ")
    current = current.next

