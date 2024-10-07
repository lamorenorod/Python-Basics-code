print("Hola")
numero1= 24
numero2= 8
resultado = numero1 + numero2
print ("La suma de numero 1 y numero 2 es:" ,resultado)

#Control Flow
# If Statements

x, y = 5, 18
if x < y:
    print('The greater is y')
else:
    print('y is less than x')




#
# LOOPS
# while

# FOR
#for local variable in your list
#for i in my list means for each elemnt, do whateveryou have inside
MyList = [5, 2, 3, 4]
for i in MyList:
    print('The value in the list is', i)


for i in range(5):
    print("HELLO WORLD")    

#we want to have eache element in the list multiplied by 2

for i in range (len(MyList)):
      MyList[i] = MyList[i]*2;
print(MyList)


#break - stops the code
#continue - it goes to infinite because its says to go back again


#DATA STRUCTURE

#Put the name with capitak letter and the rest in lower case

name = "lauRA"
type(name)

name = name[0].upper() + name[1:].lower()
print(name)

MyTuple = (1,2,3,4)
type (MyTuple)
MyTuple = (MyTuple[0],) + (5,) + MyTuple[2:]
MyTuple


#FUNCTIONS

def custom_print(text, n=1):
    for i in range(n):
        print(text)

custom_print('Hello',7)
custom_print(n=7, text=10)        


#lambda functions
bool(5%2)
bool(10%2)

#for odds
is0dd = lambda x: bool(x%2)
print('4 is odd?', is0dd(4))
print('5 is odd?', is0dd(5))


#for even
even = lambda x: not bool(x%2)
print('4 is even', even(4))
print('5 is even?', even(5))


#Get a list from the user
#print in the output the sum of the values
#together with the minimum and maximum of the values
#don't use already implemented funtion in python

nList= input()
nList = nList.split()
nList = [int (num) for num in nList]

#Lesson 4
# Third - part libraries


