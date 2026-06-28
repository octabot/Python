class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverse(head):
    # traverse
    cur = head
    while cur!=None:
        print(cur.data, end= " ")
        cur = cur.next
    print()

a = Node(11)
b = Node(12)
c = Node(13)
d = Node(14)
e = Node(15)

head = a

a.next = b
b.next = c
c.next = d
d.next = e 

traverse(head)
print(head.data)

cur = head
prev 
# nxt = None
while cur != None:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt

head = prev
traverse(head)
print(head.data)