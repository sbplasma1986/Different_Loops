# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 09:16:56 2022

@author: Suresh BASNET
"""

#Logical operators: That are used to connect more relations by
# performing operations between relations and make decision 
# which is always logical, either True or False.

#====================For 'and' operation
I1 = 10>15
#print(I1)
I2 = 10<15
#print(I2)
I3 = I1 and I2 
#print(I3)

#====================For 'or' operation
I4 = I1 or I2
#print(I4)

#======================For 'not' operation
I5 = not I1
#print(I5)

#==================if, else and elseif (elif) statements
J1 = 2
#J1 = int(input("Value of J1 = "))
J2 = 15
J3 = J1+J2

if J1 > J2:
   J4 = J3-J2+2*J1 
elif J1==J2:
  J4 = J3+J2   
else:
  J4 = J2*J1
#print(J4)

#==for loop (definite loop, we already know about number of running times.)

#for i in range(1,20,2):
   #print(i)
       
# for k in range(10):
#     print(k)    
    
#===============To print message
# for j in range(5):
#     print("Hello Suresh, how are you?")
    
#==========for the output in same single line
# for j in range(5):
#     print("Hello Suresh, how are you", end = " ")   

#===========making list using for loop
# A1 = [10, 15, 20.0, 25.2, 30, 35, 40]
# A2 = []
# for y in A1:
#    A2.append(y**2)
# print(A2)    
    

#while loop (indefinite loop, we couldn't aware about the number 
#of times run.)

# a1 = int(input("Value of a1 = "))
# while a1<=10:
#     print(a1)
#     a1 = a1+2

#============To print the message
# y = int(input("Value of y = "))
# while y<=15:
#     print("Hello Suresh")
#     y = y+2
    
#========Uses of break statement in while loop
# j = int(input("Give the value of j = "))
# while j<=20:
#     print(j)
#     j=j+2
#     if j>=13:
#         break
    
#============== Thank you and see you soon.   


#=========================================================================



#####Making Function
#==================Defining function (A function is group of
 # related statements which performs a particular assign task. When the
 # coding in the python becomes extended in larger form, it helps
 # us to organize such codes without repetition.)
 
#================making simple functions 
#def blessings():
    #print("I would like to extend my blessing to all the individuals")
    #print("Good luck")
#blessings()

#==============Calculation of x and y coodinates using y = mx+c

#c = float(input("value of c = "))
#def stline(x,m):
    #y = m*x+c
    #return y

#y1= stline(2,-0.5)
#print(y1)

#=============Add, substraction, and multiplication using function
#a = 2;
#b = 3;
#def Math_op(x,y):
    #Z1 = a*x+b*y
    #Z2 = a*x-b*y
    #Z3 = a*x*1/(b*y)
    #return Z1, Z2, Z3
#Z1, Z2, Z3 = Math_op(5,6)
#print(Z1,Z2,Z3)

#==============Thank you and that much for today, see you soon.

  
    
    






 