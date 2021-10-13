class Cat:
    def __init__(self, name , age , weight):
        self.name= name
        self.age = age
        self.weight = weight

    def walk(self):
        if self.weight <=1:
            print("cat can not walk ")
        else:
            self.weight -= 1



cat1 = Cat("OLD TOM", 6, 1)
cat2 = Cat("Olli", 5, 10)
cat3 = Cat("bolli", 4, 10)

cat1.walk()
cat2.walk()
cat3.walk()

print(cat1.weight)
print("cat 2 weight is :" + str(cat2.weight))
print("cat 3 weight is :" + str(cat3.weight))