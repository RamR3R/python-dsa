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



current = head
count = 0
while current != None:
    # print(current.val)
    current = current.next
    count += 1
print(count)



