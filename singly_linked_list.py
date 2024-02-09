"""
Linked list: It is a linear data stracture, in which elements are not stored at a contiguous location, rather they are linked using pointers.
Advantages: 1. Dynamic Data Stracture: The size of the memory can be allocated or de-allocated at run time based on operation.
            2. Ease of insertation or deletation: Insertation and deletation are simpler than array.
            3. Efficient Memory Utilization: It use memory as per need.
            4. Implementation: Various data structure can be implemented using linked list like stack, queue, graph, maps etc.
Disadvantages: 1. Random Access: Unlike array, linked list doesn't allow direct access by index.
               2. Extra Memory: It require extra memory for storing the pointers, compared to array.
Linked List VS Arry: 1. Location: Array stored contiguous location | Linked List are not.
                     2. Size: Array is fixed in size | Linked List are Dynamic in size.
                     3. Memory Allocation: Array allocates memory in compile time | Linked List allocates memory in runtime.
                     4. Element Access: Element can access easily in array | Element access requires traversal in Linked List.
                     5. Insert & Delete: Array takes long time in insertation & deletation | Linked List is faster than Array.
Time Complexity Singly Linked List vs Array:
                    Operation               |  Array  | Linked List
                    Insert,Delete at index  |   O(1)  |   O(N)
                    Insert,Delete at head   |   O(N)  |   O(1) -> Tracking Head
                    Insert,Delete at tail   |   O(1)  |   O(N) * O(1) if we track tail
"""
# Node Stracture
class Node:
    def __init__(self, data = None, next = None): # constructor
        self.data = data
        self.next = next

# Creating Nodes
node1 = Node(10) # 10 | None
node2 = Node(20) # 20 | None
node3 = Node(30) # 30 | None
node4 = Node(40) # 40 | None

# Creating Connection to form a linked list
node1.next = node2 # 10 | Address of node2
node2.next = node3 # 20 | Address of node3
node3.next = node4 # 30 | Address of node4

# Creating Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at head
    def insert_at_head(self, data): # Time Complexity O(1)
        newNode = Node(data, self.head)
        self.head = newNode

    # Insert at tail
    def insert_at_tail(self, data): # Time Complexity O(N)
        if self.head is None:
            self.head = Node(data,None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data, None)

    # Insert a list of data
    def insert_list(self, data_list):
        for data in data_list:
            self.insert_at_tail(data)

    # Length of linked list
    def len(self): # Time Complexity O(N)
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length
    
    # Insert at index
    def insert_at_index(self, index, data):
        if index < 0 or index >= self.len():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_head(data)
            return
        count = 0
        temp = self.head
        while temp:
            if count == index-1:
                newNode = Node(data, temp.next)
                temp.next = newNode
                break
            temp = temp.next
            count += 1
    
    # Remove at index
    def remove_at_index(self, index):
        if index < 0 or index >= self.len():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return # In python it auto delete garbage, in c or c++ you should delete it menually.
        count = 0
        temp = self.head
        while temp:
            if count == index-1:
                deleteNode = temp.next
                temp.next = deleteNode.next
                break
            temp = temp.next
            count += 1

    # Printing linked list
    def print(self):
        if self.head is None:
            print('Empty Linked List')
            return
        llstr = ''
        temp = self.head
        while temp:
            llstr += str(temp.data) + '->'
            temp = temp.next
        print(llstr)

# Sample Operations
ll = LinkedList()
ll.insert_at_head(5)
ll.insert_at_head(89)
ll.insert_at_tail(7)
ll.insert_list(['a', 'b'])

print(ll.len())
ll.print()
ll.remove_at_index(1)
ll.print()
ll.insert_at_index(2, 'Tanzid')
ll.print()