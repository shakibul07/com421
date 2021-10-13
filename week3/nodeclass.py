
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

n1 = Node("fred")
n2 = Node("Tom")

print(n1)

n1.link(n2)
print(n1.prev)
print(n1.next)
print(n2.prev)
print(n2.next)
