class Cat:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def eat(self):
        self.weight += 3

cat1 = Cat("binnie", 4 , 4)
cat2 = Cat("clyde", 1, 2)

print(str(cat1.name) + " weight before eating = " + str(cat1.weight))
print(str(cat2.name) + " weight before eating = " + str(cat2.weight))


cat1.eat()
cat2.eat()

print(str(cat1.name) + " weight after eating = "+ str(cat1.weight))
print(str(cat2.name) + " weight after eating = "+str(cat2.weight))
