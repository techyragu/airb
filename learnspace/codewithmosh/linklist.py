class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LL:
    def __init__(self):
        self.head = None

    def add(self, val):
        node = Node()
        node.val = val

        if self.head is None:
            self.head = node
            return
        
        prev = None
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next

        prev.next = node

    def __str__(self):
        curr = self.head
        lstr = ""
        while curr:
            lstr += str(curr.val) + " > "
            curr = curr.next

        return lstr
    
def oddEvenList(head):
    odd = head
    even = head.next
    even_head = head.next

    while odd and even:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = even_head
    
    return head

ll = LL()    
for i in range(1,6):
    ll.add(i)
print(ll)

nll = LL()
nll.head = oddEvenList(ll.head)
print(nll)



