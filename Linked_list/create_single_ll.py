class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # this method is commented out, but it can be used for iteration
    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         node = node.next

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
    
    # insert in Singly Linked List
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
                if location == 0:
                    newNode.next = self.head
                    self.head = newNode
                elif location == 1:
                    newNode.next = None
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
    
    # Time and space complexity O(n) and O(1)
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    # Time and space complexity O(n) and O(1)
    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return True, index
            current = current.next
            index += 1
        return False


singleLinkedList = SLinkedList()
singleLinkedList.insert(1, 1) 
singleLinkedList.insert(2, 1)
singleLinkedList.insert(3, 1)
singleLinkedList.insert(4, 3)

# print([node.value for node in singleLinkedList]) # This will print the values in the linked list
print(singleLinkedList)  # This will print the linked list in a readable format
singleLinkedList.traverse()
print(singleLinkedList.search(3))