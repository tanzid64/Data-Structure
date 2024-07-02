
# Node Stracture
class Node:
    """
    This class represents a Node in a singly linked list.
    Each node has two attributes:
    - data: The value stored in the node.
    - next: A reference to the next node in the linked list.
    """
    def __init__(self, data = None, next = None): # constructor
        """
        Initializes a new Node object.
        Args:
            data (Any): The value to be stored in the node.
            next (Node): The next node in the linked list.
        """
        # Assign the given data to the node's data attribute.
        self.data = data
        # Assign the given next node to the node's next attribute.
        self.next = next

# Creating Linked List
class LinkedList:
    def __init__(self):
        """
        Initializes a new LinkedList object.
        This function initializes a new LinkedList object. It creates a new LinkedList 
        object and assigns None to its head attribute. This head attribute is used to 
        store the reference to the first node in the linked list.
        """
        
        # Assign None to the head attribute.
        # The head attribute is used to store the reference to the first node in the linked list.
        # By default, the head attribute is None, indicating that the linked list is empty.
        self.head = None

    # Insert at head
    def insert_at_head(self, data): # Time Complexity O(1)
        # Create a new node with the given data and the current head of the linked list.
        # The new node will become the new head of the linked list.
        
        # Create a new node with the given data and the current head of the linked list.
        # The new node's next attribute will be set to the current head of the linked list.
        newNode = Node(data, self.head)
        
        # Set the head attribute of the linked list to the new node.
        # This makes the new node the new head of the linked list.
        self.head = newNode

    # Insert at tail
    def insert_at_tail(self, data): # Time Complexity O(N)
        # If the linked list is empty, create a new node with the given data and assign it to the head.
        if self.head is None:
            self.head = Node(data, None)
            return
        
        # Traverse through the linked list to find the last node.
        temp = self.head
        while temp.next:
            temp = temp.next
        
        # Create a new node with the given data and assign it as the next node of the last node.
        temp.next = Node(data, None)

    # Insert a list of data
    def insert_list(self, data_list):
        """
        This function takes in a list of data and inserts each item in the list
        at the end of the linked list.

        Parameters:
        - data_list (list): A list of data to be inserted into the linked list.

        Returns:
        - None
        """

        # Iterate through each item in the input list
        for data in data_list:
            # Insert the current item at the end of the linked list
            
            # Insert the current item at the end of the linked list.
            # This is done by calling the insert_at_tail method which adds a new node
            # with the given data at the end of the linked list.
            self.insert_at_tail(data)

    # Length of linked list
    def len(self): # Time Complexity O(N)
        """
        This function returns the length of the linked list.
        
        Parameters:
        - None
        
        Returns:
        - int: The length of the linked list.
        """
        
        # Initialize a variable to keep track of the length of the linked list.
        # This variable is initialized to 0.
        length = 0
        
        # Initialize a variable to keep track of the current node.
        # This variable is initialized to the head of the linked list.
        temp = self.head
        
        # Traverse through the linked list.
        # This is done by iterating through each node in the linked list.
        while temp:
            # Increment the length variable by 1 for each node encountered.
            length += 1
            
            # Move to the next node in the linked list.
            temp = temp.next
        
        # Return the length of the linked list.
        return length
    
    # Insert at index
    def insert_at_index(self, index, data):
        """
        Insert a node at a specific index in the linked list.
        If the index is invalid, raise an Exception.
        If the index is 0, insert the node at the head of the linked list.
        
        Args:
            index (int): The index at which to insert the node.
            data (Any): The data to be inserted into the node.
        
        Raises:
            Exception: If the index is invalid.
        """
        
        # Check if the index is in a valid range.
        if index < 0 or index >= self.len():
            raise Exception("Invalid index")
        
        # Check if the index is at the head of the linked list.
        if index == 0:
            self.insert_at_head(data)
            return
        
        # Initialize a variable to keep track of the current node.
        # This variable is initialized to the head of the linked list.
        count = 0
        temp = self.head
        
        # Traverse through the linked list.
        # This is done by iterating through each node in the linked list.
        while temp:
            # Check if the current index is the index at which to insert the node.
            if count == index-1:
                # Create a new node with the given data and the next node of the current node.
                # The new node will be inserted between the current node and the next node.
                newNode = Node(data, temp.next)
                
                # Set the next attribute of the current node to the new node.
                # This makes the new node the next node of the current node.
                temp.next = newNode
                
                # Exit the loop, as the node has been inserted at the correct index.
                break
            
            # Move to the next node in the linked list.
            temp = temp.next
            
            # Increment the count variable by 1 for each node encountered.
            count += 1
    
    # Remove at index
    def remove_at_index(self, index):
        # Check if the index is in a valid range.
        if index < 0 or index >= self.len():
            raise Exception("Invalid index")
        
        # Check if the index is at the head of the linked list.
        if index == 0:
            # If the index is at the head, update the head to the next node.
            # This effectively removes the first node from the linked list.
            self.head = self.head.next
            return  # In Python, Python automatically handles garbage collection, so we don't need to manually delete the node.
            # In C or C++, we would need to manually delete the node.
        
        # Initialize a variable to keep track of the current node.
        # This variable is initialized to the head of the linked list.
        count = 0
        temp = self.head
        
        # Traverse through the linked list.
        # This is done by iterating through each node in the linked list.
        while temp:
            # Check if the current index is the index at which to remove the node.
            if count == index-1:
                # Store a reference to the node to be deleted.
                deleteNode = temp.next
                
                # Update the next attribute of the current node to the next node after the node to be deleted.
                # This effectively removes the node to be deleted from the linked list.
                temp.next = deleteNode.next
                
                # Exit the loop, as the node has been removed at the correct index.
                break
            
            # Move to the next node in the linked list.
            temp = temp.next
            
            # Increment the count variable by 1 for each node encountered.
            count += 1

    # Printing linked list
    def print(self):
        """
        This function prints the linked list.
        
        Parameters:
        - None
        
        Returns:
        - None
        
        This function checks if the head of the linked list is None. 
        If it is, it prints 'Empty Linked List' and returns.
        
        If the head is not None, it initializes an empty string called llstr.
        It then initializes a variable called temp to the head of the linked list.
        
        The function then enters a while loop that continues until temp is None.
        Inside the loop, it appends the data attribute of the temp node to the llstr string,
        followed by '->'. It then updates temp to the next node in the linked list.
        
        After the loop has finished, it prints the llstr string.
        """
        if self.head is None:
            print('Empty Linked List')
            return
        
        # Initialize an empty string to store the linked list elements
        llstr = ''
        
        # Initialize a variable to keep track of the current node.
        # This variable is initialized to the head of the linked list.
        temp = self.head
        
        # Traverse through the linked list.
        # This is done by iterating through each node in the linked list.
        while temp:
            # Append the data attribute of the current node to the llstr string.
            # This effectively adds the data of the current node to the string.
            llstr += str(temp.data) + '->'
            
            # Move to the next node in the linked list.
            temp = temp.next
        
        # Print the llstr string.
        # This effectively prints the elements of the linked list.
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