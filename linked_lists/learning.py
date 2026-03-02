# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null

#Linked List class
class LinkedList:

    #Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    # This function prints content of linked list starting
    # from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    list = LinkedList()

    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    list.head.next = second; #Link first node with second

    second.next = third; # Link second node with the third

    list.printList()