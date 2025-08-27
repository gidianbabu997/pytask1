# # # name = input("Enter your name: ")
# # # age = input("Enter your age: ")
# # # city = input("Enter your city: ")

# # # print("Name:", name, "| Age:", age, "| City:", city)

# # ids=[1,2,334432,233,]
# # print(type(ids))
# # print(type(ids))


# fruits=["apple", "mango", "orange", "banana", "gova"]
# print(id(fruits))
# print(len(fruits))
# print(fruits[2])
# print(fruits[-2])
# # print(f"length of the fruits colletions is {len(fruits)}")

# fruits[2]='ram'
# print(id(fruits))


# fruits[len(fruits)]=5
# print(fruits)

# x=[]+[6]
# x[len(x)]=5
# print(x)


# list=[1,23,34,44,'hi']
# op=list+[12,34,324]
# print(op)

fruits=["apple","mango","banana"]
print(fruits[0],fruits[2]) #printing the 1st and last fruits
print(len(fruits)) #print the total number of fruits
fruits[1]="pineapple"
print(fruits) #replacing the mango with pineapple

x=["harish","naresh","suresh","mahesh"]
print(id(x)) #printing the id of X
x[2]="kiran"
print(x) #updated suresh to kiran
print(id(x)) #afer the changes id printed

data=[1,2,[4,5],[6,7],8,"something"]
print(data[2][0]) #printed the 4 in the nested list
print(data[3][0]) #printed the 6 in the nested list
print(data[5][2]) #letter m printed from something string

mixed=[1,2,"hi",122.5,"true"]
print(type(mixed))
print(type(mixed[1])) #printed the type
print(type(mixed[2]))

