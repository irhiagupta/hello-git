# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 23:38:55 2018

@author: Rhia
"""


#Question 1: Create a list with user defined inputs
lists=input("Enter the expression: ")
lists=lists.split()
print(lists)

#Question 2: Add a list to above list
l2=['google', 'apple', 'facebook', 'microsoft', 'tesla']
print(l2)
lists.extend(l2)
print(lists)


#Question 3: count the number of time the item occus in the list
print('Count of Google: ', lists.count('google'))
for x in lists:
   print("{}: {}".format(x,lists.count(x)))
   


#Question 4:
num=[1,2,341,4,1,55]
num.sort()
print(num)
   


#Question 5: merge two array into third array and sort them ascending order
A=[35,2,52,6,84]
B=[52,62,8,1,7,3,67]
print("A: ", A)
print("B: ", B)
c=[]
c.extend(A)
c.extend(B)
c.sort() 
print("Combined and sorted list of numbers: ",c)




#Question 6: Stacks and Queues implementation
print("STACKS\n")
stack=['Rhia', 'Riya', 'Priyanshi', 'Ridhi', 'Ridham']
print(stack)
stack.append('Ankita')
print(stack)
stack.append('Amrita')
print(stack)
print("Popping: ",stack.pop())
print(stack)
print("Popping: ",stack.pop())



print("Queues\n")
queues=['Rhia','priya','riya','ridhi']
queues.append('Amrita')
print(queues)
print("Popping: ", queues.pop(0))
print(queues)




#Question Optional: even/odd numbers in the list
num=[1,2,3,5,15,5,11,56,7]
print("Numbers are: ",num)
e=[]
o=[]
for x in num:
    if x%2==0:
        e.append(x)
    else:
        o.append(x)
print("Even numbers: ", e)
print("Odd numbers: ",o)
    
    
