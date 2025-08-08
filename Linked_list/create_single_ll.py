class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
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
                elif location >= self.length:
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
        self.length += 1
    
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

    # This function takes index as parameter and return the value from it's location.
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # Time and space complexity O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value

    # Time and space complexity O(n) and O(1)
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        self.length -= 1
        return popped_node

    # Time and space complexity O(n) and O(1)
    def remove(self,index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1 or index == -1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    # In Python, garbage collection automatically delete if it's not point to any element one by one.
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def reverse(self):
        pre_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail,self.head

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
    def remove_duplicates(self):
        if self.head is None:
            return
        node_set = set()
        current_node = self.head
        node_set.add(current_node)

        while current_node.next:
            if current_node.next.value in node_set:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_set.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

singleLinkedList = SLinkedList()
singleLinkedList.insert(1, 1) 
singleLinkedList.insert(2, 1)
singleLinkedList.insert(2, 1)
singleLinkedList.insert(4, 4)
singleLinkedList.insert(4, 4)
singleLinkedList.insert(5, 4)

# print([node.value for node in singleLinkedList]) # This will print the values in the linked list
print(singleLinkedList)  # This will print the linked list in a readable format
# singleLinkedList.traverse()
# print(singleLinkedList.search(3))
# print(singleLinkedList.set_value(2,10))
# print(singleLinkedList.remove(3))
# print(singleLinkedList.length)
# singleLinkedList.reverse()
print(singleLinkedList.remove_duplicates())
print(singleLinkedList)