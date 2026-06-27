class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(11)
# a.next = b         -> b is not created yet
b = Node(12)
# a.next = b        -> it works
c = Node(13)
d = Node(14)
e = Node(15)

a.next = b
b.next = c
c.next = d
d.next = e

# traverse
cur = a
while cur!=None:
    print(cur.data, end= " ")
    cur = cur.next