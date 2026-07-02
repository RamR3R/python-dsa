class Node:
    def __init__(self):
        self.val = 0
        self.next = None
        self.prev = None

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

#travesal before delete
current = head
while current != None:
    print(current.val , end= " => ")
    current = current.next
print()



#delete at head
# head = head.next

#delete at tail
# current = head
# while current.next.next != None:
#     current = current.next

# current.next = None

#delete on position
position = int(input("Enter the position to delte : "))
count = 1
current = head
while count < position - 1:
    current = current.next
    count += 1

current.next = current.next.next







#travesal after delete
current = head
while current != None:
    print(current.val , end= " => ")
    current = current.next