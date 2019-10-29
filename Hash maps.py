# The following program is the solution to the String Keys Practice quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        index = self.calculate_hash_value(string)
        self.table[index] = string
        

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        index = self.calculate_hash_value(string)
        if self.table[index] == string:
            return index
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hash_value = (ord(string[0])*100) + ord(string[1])
        return hash_value 
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

## Test store edge case
hash_table.store('UDACIOUS')
## Should be 8568
print(hash_table.lookup('UDACIOUS'))
