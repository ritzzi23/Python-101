#Strings Tutorial
a = 'I am single'
b = "I am single"
c = """I am single"""

print(a)
print(b)
print(c)

#if want to use single qoute in a string element defined using single qoutes('') 
#use escape character (\)

d = 'I don\'t want water'

print(d)

#functions related to strings

#1.finding length of a string 

f= 'I love katrina'
print(len(f))

#2.Concatenation of two strings
print(a+' and '+d)

#3.To concatenate a string and a number

v=25
print(f+ str(v))

#4.To print a string n number of times

print(f * 10)
 
