class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class create_ssl:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
    
    def insert(self,val,location):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode = self.head
                self.head = newNode
            elif location >= self.length:
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = None
            else:
                temp = self.head
                index = 0
                while index<location-1:
                    temp = temp.next
                    index += 1
                next = temp.next
                temp.next = newNode
                newNode.next = next
        self.length += 1
    
    def merge(self,l1,l2):
        prehead = ListNode(-1)

        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        prev.next = l1 if l1 is not None else l2

        return prehead.next



create1 = create_ssl()
create1.insert(1, 1) 
create1.insert(3, 2)
create1.insert(8, 3)
create1.insert(11, 4)
create1.insert(14, 5)


create2 = create_ssl()
create2.insert(2, 1) 
create2.insert(4, 2)
create2.insert(6, 3)
create2.insert(9, 4)

join = create_ssl()
join.head = join.merge(create1.head, create2.head)
print(join)



