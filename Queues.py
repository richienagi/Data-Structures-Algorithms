# The following program is the solution to the Queue Practice quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

print(q.storage)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
print(q.storage)
# Should be 2
print(q.dequeue())
print(q.storage)
# Should be 3
print(q.dequeue())
print(q.storage)
# Should be 4
print(q.dequeue())
q.enqueue(5)
print(q.storage)
# Should be 5
print(q.peek())
