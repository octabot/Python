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
print(a.next) #None bcz a.next is not assigned yet
print(b.data) #value = 7
print(b.next)
a.next = b # a.next is assigned
print(a.data)
print(b)  #address of b
print(a.next)  #address of b

print("\n")
head = a
print(head.data)