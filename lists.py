#Lists-collection of values

#1-Declaration
names =[]

#2-Assigning Values
names = ["mark","john","jaq"]

print(names)


#3-To print a specific element
#value starts from [0,1,2..]

print(names[2])


#4-Element can be accessed in reverse order also.
#reverse value starts from [..,-3,-2,-1]

print(names[-2])


#5-Append Function - This function is used to add values in a existing list.

names.append("katrina")

print(names)


#Extend Function-To join two diffenrt lists.
age = [23,12,32,11]

names.extend(age)

print(names)

#6-Remove- to remove a particular value from list.

names.remove("john")

print (names)

#7-To print two lists at once 

print(names, age)


#8-Length-to find the lentgth of a list.

print(len(names))

#9-Max-to find the maximum of a list.

print(max(age))
