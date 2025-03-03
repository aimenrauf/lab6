class Node:
    def __init__(self,name,time):
        self.name = name
        self.time = time
        self.remain_time = time
        self.next = None
class RoundRobin:
    def __init__(self,time_quantum):
        self.head = None
        self.time_qunatum = time_quantum
    def append(self,name,time):
        process  = Node(name,time)
        if self.head is None:
            self.head = process
            self.head.next = process
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = process
            process.next = self.head
    def display(self):
        current = self.head
        while True:
            print(f"- {current.name}: {current.time} ms")
            current = current.next
            if current == self.head:
                break
    def execution(self):
        if self.head is None:
            print("No process to schedule")
            return
        current = self.head
        while True:
            if current.remain_time > 0:
                execute_time = min(self.time_qunatum,current.remain_time)
                current.remain_time -= execute_time
                print(f"- Running {current.name} for {execute_time}ms (Remaining: {current.remain_time}ms)")
                if current.remain_time == 0:
                    print(f" Process {current.name} is completed")
                if self.all_process():
                    break
            current = current.next
    def all_process(self):
        current = self.head
        while True:
            if current.remain_time > 0:
                return False
            current = current.next
            if current  == self.head:
                break
        return True
RR = RoundRobin(3)
RR.append("Word",10)
RR.append("WHatsapp",5)
RR.append("VSCode",7)
RR.display()
RR.execution()