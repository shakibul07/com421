print("what is your cat1 name ?  ")
namecat1 = input()
print("what is your cat1 age ?  ")
agecat1 = int(input())
print("what is your cat1 weight  ?  ")
weightcat1 = int(input())


print("what is your cat2 name ? ")
namecat2 = input()
print("what is your cat2 age ?  ")
agecat2 = int(input())
print("what is your cat2 weight  ?  ")
weightcat2 = int(input())


print("what is your cat3 name ?  ")
namecat3 = input()
print("what is your cat3 age ?  ")
agecat3 = int(input())
print("what is your cat3 weight  ?  ")
weightcat3 = int(input())



if weightcat1 > 1:
    print(namecat1 + " weight after walk is " + str(weightcat1 - 1 ))

else:
    print(namecat1 + " is starving. feed some food")



if weightcat2 > 1:
    print(namecat2+ " weight after walk is " + str(weightcat2 - 1))

else:
    print(namecat2 + " is starving. feed some food")



if weightcat3 > 1:
    print(namecat3 + " weight after walk is " + str(weightcat3 - 1))

else:
    print(namecat3 + "cat is starving. feed some food")