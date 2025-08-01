# Time and Space Complexity:
# Time Complexity: O(1) for creating a node.
# Space Complexity: O(n) for storing n nodes in the linked list. now it's O(1) since we have two nodes.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
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
            elif location == -1:
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


singleLinkedList = SLinkedList()
singleLinkedList.insert(1, 1) 
singleLinkedList.insert(2, 1)
singleLinkedList.insert(3, 1)
singleLinkedList.insert(0, 0)
singleLinkedList.insert(0, 3)
# node1 = Node(1)
# node2 = Node(2)

# singleLinkedList.head = node1
# singleLinkedList.head.next = node2
# singleLinkedList.tail = node2

print([node.value for node in singleLinkedList])



