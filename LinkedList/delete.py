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

# delete from start
head = head.next
traverse(head)

# delete from last
cur = head
while cur.next.next!= None:
    cur = cur.next                  #move one step ahead with every iteration
cur.next = None
traverse(head)

# delete from kth position 
k = 1
cur = head
for i in range(k-1):
    cur = cur.next
cur.next = cur.next.next
traverse(head)