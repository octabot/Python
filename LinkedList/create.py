class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a =  Node(5)
print(a) #address of a
print(a.data) #value = 5
print(a.next)
b = Node(7)
print(b) #address of b
print(b.data) #value = 7
print(b.next)
a.next = b
print(a.data)
print("\n\n")
head = a
print(head.data)