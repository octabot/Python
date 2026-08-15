'''
In many languages, a variable created inside a loop is "born 
and dies" inside that loop (block scope). If you tried to use 

it outside the loop, the program would crash.
Python is different. It has function scope, not block scope. 
A variable created inside a while loop or an if statement is 
perfectly accessible anywhere else inside that same function, 
even after the loop finishes.
'''

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
prev = None
# nxt = None
while cur != None:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt

head = prev
traverse(head)
print(head.data)