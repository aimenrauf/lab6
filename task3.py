class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CicularLinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  
        else:
            current= self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  
    def display(self):
        current = self.head
        while True:
            print(current.data, end="-> ")
            current = current.next
            if current == self.head:
                break
        print("Back to head")
    def execute(self, cycles):        
        current = self.head
        for _ in range(cycles):  
            print(current.data, end="-> ")
            current = current.next
link = CicularLinkedList()
data = ["Lab tasks","Home tasks","watching Tv"]
for n in data:
    link.append(n)
link.display()
link.execute(10)