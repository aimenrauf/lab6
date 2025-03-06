class Node:
    def __init__(self, sender, message):
        self.sender = sender
        self.message = message
        self.next = None
        self.prev = None

class ChatHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None 

    def send_message(self, sender, message):
        new_node = Node(sender, message)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_chat(self):
        if not self.head:
            print("No chat history.")
            return
        current = self.head
        print("\n Chat History:")
        while current:
            print(f"{current.sender}: {current.message}")
            current = current.next

    def delete_message(self, message):
        current = self.head
        while current:
            if current.message == message:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next 

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev 

                print(f" Deleted message: {message}")
                return
            current = current.next
        print(" Message not found.")

    def navigate_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f" Next Message: {self.current.sender}: {self.current.message}")
        else:
            print(" No more messages ahead.")

    def navigate_prev(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f" Previous Message: {self.current.sender}: {self.current.message}")
        else:
            print(" No previous messages.")
chat = ChatHistory()
chat.send_message("Aimen", "AOA! How are you? ")
chat.send_message("Haseeb", "I'm good, how about you?")
chat.send_message("Aimen", "I'm fine too. What are you up to?")
chat.send_message("Haseeb", "Just working on some code! ")
chat.display_chat()
chat.navigate_next()  
chat.navigate_prev()  
chat.delete_message("I'm fine too. What are you up to?")
chat.display_chat()