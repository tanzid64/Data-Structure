"""
LIFO Pattern = Last in first out
Example: Undo function in any editor use stack data structure.

Time Complexity:
push O(1)
pop O(1)
top O(1)
size O(N)
isEmpty O(1)
display O(N)

Space Complexity:
All operation O(1)
"""

class Node:
    def __init__(self, data = None, next = None, prev = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        newNode = Node(data, self.head, None)
        self.head.prev = newNode
        self.head = newNode

    def pop(self):
        if self.head is None:
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        data = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return data
    
    def top(self):
        return self.head.data
    
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def display(self):
        if self.head is None:
            print("Stack is Empty")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print()


