# The following program is the solution to the Python Practice quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

class Classy:
    def __init__(self):
        self.items = []
        
    
    def addItem(self,fashion):
        self.items.append(fashion)
    
    def getClassiness(self):
        self.classiness = 0
        for i in self.items:
            if i == "tophat":
                self.classiness = self.classiness + 2
            if i == "bowtie":
                self.classiness = self.classiness + 4
            if i == "monocle":
                self.classiness = self.classiness + 5    
        return self.classiness


# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem('tophat')
# Should be 2
print(me.getClassiness())

me.addItem('bowtie')
me.addItem('jacket')
me.addItem('monocle')
# Should be 11
print(me.getClassiness())

me.addItem('bowtie')
# Should be 15
print(me.getClassiness())
print(me.items)
