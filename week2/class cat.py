#exercise 1 week 2

class Cat:
    def __init__(self,name, weight, age):
        self.name = name
        self.age = age
        self.weight = weight


    def eat(self):
        self.weight += 1

    def walk(self):
      self.weight -= 1



cat1 = Cat("OLD TOM", 6, 10)
cat2 = Cat("Olli", 5, 10)
cat3 = Cat("bolli", 4, 10)


print("cat 1 before weight " + str(cat1.weight))
print("cat 2 before weight " + str(cat2.weight))
print("cat 3 before weight " + str(cat3.weight))


cat1.walk()
cat2.walk()
cat3.walk()

print("cat 1 weight is " + str(cat1.weight))
print("cat 2 weight is " + str(cat2.weight))
print("cat 1 weight is " + str(cat3.weight))
