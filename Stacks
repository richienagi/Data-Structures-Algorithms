# The following program is the solution to the Stacks Practice quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

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

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_node = Element(new_element)
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        first_element = self.head
        new_head = self.head.next
        self.head.next = None
        self.head = new_head
        return first_element
    
    def display(self):
        elems = []
        current = self.head
        while current != None:
            elems.append(current.value)
            current = current.next
        print(elems)

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element.value)
        
    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        if self.ll.head == None:
            return None
        return self.ll.delete_first()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

#Testing
#lllist = LinkedList(e1)
#lllist.append(e2)
#lllist.append(e3)
#lllist.append(e4)
#lllist.display()
#lllist.insert_first(9)
#lllist.display()
#print(lllist.delete_first().value)
#lllist.display()

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
stack.ll.display()

print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
