# The following program is the solution to the Linked List quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        cur_idx = 1
        current = self.head
        while True:
            if cur_idx == position:
                return current
            cur_idx = cur_idx + 1
            current = current.next
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        cur_idx = 1
        new_node = new_element
        cur = self.head
        while cur.next != None:
            if cur_idx == position-1:
                last_node = cur.next
                cur.next = new_node
                cur.next.next = last_node
            cur = cur.next
            cur_idx = cur_idx + 1
        #cur.next = new_node
    
    def delete(self, value):
        """Delete the first node with a given value."""
        cur = self.head
        if cur.value == value:
           self.head = cur.next
           cur = None
           return
        prev = None
        while cur != None and cur.value != value:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None
               
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            elems.append(cur_node.value)
            cur_node = cur_node.next
        if cur_node.next == None:
            elems.append(cur_node.value)
        print(elems)
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

#ll.display()

# Test get_position
# Should print 3
#print(ll.head.next.next.value)
# Should also print 3
#print(ll.get_position(3).value)
#
## Test insert
ll.insert(e4,3)
ll.display()
## Should print 4 now
print(ll.get_position(3).value)
#
## Test delete
ll.delete(1)
ll.display()
## Should print 2 now
print(ll.get_position(1).value)
## Should print 4 now
print(ll.get_position(2).value)
## Should print 3 now
print(ll.get_position(3).value)
