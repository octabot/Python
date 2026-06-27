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

# Insert At first
f = Node(10)
f.next = head
head = f

traverse(head)

# Insert At Last
l = Node(16)

cur = head
while cur.next!= None:
    cur = cur.next 
cur.next = l

traverse(head)

# Insert at k index ->  k=2
k= 2
n = Node(11.5)
cur = head 
for i in range(k-1):
    cur = cur.next

n.next = cur.next.next
cur.next = n

traverse(head)