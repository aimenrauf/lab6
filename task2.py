class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class CicularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.head.next = self.head  
        else:
            current= self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head  
    def delete(self,data):
        current = self.head
        prev = None
        if current.data == data:
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:  
                self.head = None
            else:
                current.next = self.head.next  
                self.head = self.head.next 
            return
        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == data:
                prev.next = current.next
                return
    def display(self):
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print("Back to head")
link = CicularLinkedList()
data = [1,2,3,4,0]
for n in data:
    link.append(n)
link.display()
link.delete(1)
link.display()