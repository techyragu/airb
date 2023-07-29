# LRU is key-value pair cache
# limited capacity
# Evict Policy - Least recently used
# Get from cache 0(1) - Dict should get/update value in 0(1)
# Now how do I know if its last added or recently added ,  Queue should solve it
# but now get in 0(n)
# Lets say capcity of 3
# add 1, 2, 3 
# get 2 then 2 should become recent -> 1,3,2 
#  add 4 , 1 should be removed and 4 should be added 3,2,4

class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        s = ""
        if self.prev:
            s += f"{self.prev.key} <- "
        s += str(self.key)
        if self.next:
            s += f" <- {self.next.key} "
        return s

class LRU:
    def __init__(self, capacity) -> None:
        self.cap = capacity
        self.cache = {}
        self.head = Node(10,10)
        self.tail = Node(20,20)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _addNode(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        #print(f"add node {node.key}, {node}")

    def _removeNode(self, node):
        # node1 - node - node2
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def add(self, key, val):
        if key not in self.cache:
            node = Node(key,val)
            if len(self.cache) < self.cap:
                self.cache[key]=node
                # add node in list 
                self._addNode(node)
            else:
                # get the least recently used node
                # del from cache
                lruNode = self.head.next
                del self.cache[lruNode.key]
                # remove node from list
                self._removeNode(lruNode)
                # add new node to list
                self.cache[key]=node
                self._addNode(node)
        else: # key not in cache
            # get existing node from cache
            node = self.cache[key]
            node.value = val # updated new value

            # remove from list
            self._removeNode(node)
            # append to list
            self._addNode(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # remove from list
        self._removeNode(node)
        # append to list
        self._addNode(node)
        return node.value
    
    def display(self):
        print(self.cache)
        #print(self.head)
        cur = self.head.next
        #print(cur)
        while cur is not None:
            #print(f"cur: {cur}")
            print(cur.key, end='<-')
            cur = cur.next
        print("====")

    
if __name__ == "__main__":
    print("Starting")
    lru = LRU(3)
    lru.display()
    lru.add(1, 1)
    lru.display()
    lru.add(2, 2)
    lru.display()
    lru.add(3, 3)
    lru.display()
    lru.add(4, 4)
    lru.display()
    lru.get(2)
    lru.display()
    lru.add(5, 5)
    lru.display()