
class Node:
    def __init__(self,data):
         self.data =data
         self.prev = None
         self.next = None

    def link(self, newNode):
        self.next = newNode
        newNode.prev = self

    def __str__(self):
        return self.data.__str__()


class LinkedList:
    def __init__(self,data):
        self.data = data
        self.first = None
        self.last = None

    def addNode(self,newNode):
        if (self.first == None or self.last == None):
            self.first = newNode
            self.last = newNode
        else:
            self.last.link(newNode)
            self.last = newNode

    def get(self, Index):
        count = 1
        n = self.first

        while n is not None :
            print(count)
            count += 1
            n = n.next
        return count


n1 = Node("fred")
n2 = Node("Tom")

n1.link(n2)
print(n1.prev)
print(n1.next)
print(n2.prev)
print(n2.next)

