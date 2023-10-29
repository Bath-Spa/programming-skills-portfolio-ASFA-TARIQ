#this program is for Print function
print("This is text")

print(10/3)
print(2**5)

#This program is for Creating variable and printing it
age=21
print("You are ",age," years old") 

age=age*2
print("You are actually",age,"") 

#This program shows cancatenation
a="Hello"
b="Big" 
c="World"
print( a, " " + b, " " + c )

#This program shows cancatenation
message='Hello '+'World'
print(message)

#This program shows repetition
a="Hello" 
print(a*3) 

#This shows cancatenation
print('Enter the amount of '+
      'sales for each day and '+
      'press Enter.')

#This program is for implicit string literal cancatenation 
my_str='one' ' two' ' three'
print(my_str)

#program sample 1
#create string type variables
name="python"
print(name)
message="I love phython."
print(message)

#program sample 2
#this program prints Helo, World!
print('Hello, World!')

 #program sample 3
 #This program adds two numbers
num1=1.5
num2=6.3
#add two numbers
sum= num1+num2
#Display the sum
print('The sum of {0} and {1} is{2}'.format(num1,num2,sum))

#program sample 4
#python program to calculate the square root
#Note:change this value for a diffirent result
#num=8
# take the input from the user
num=float(input('Enter a number:'))
num_sqrt=num**0.5
print('The square root of %0.3f is %0.3f'%(num,num_sqrt))
 
print('hello')
print("bye")

#program sample 5
#Python program to assign a message to a variable 
msg="Hello,This is assigning a message to a variable program"
print(msg)

#program sample 7
#Phython code to determine escape character
#string
a="This\nis\tPhython language"
print(a)

#program sample 8
#Python code to print number
a=int(input("Enter your favorite number= ")) 
print("My favorite number is ={0}".format(a))

#program 7
#python code using stripping
#string
a="\t   Asfa Tarq    \n"
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())

#program sample 9
#python code that calculstes how manycandies he can buy and how many dollatrs he will have left
Candies_Bought=("Total candies bought are=")
money_left="Total money that is left="
print(Candies_Bought+str(int(20/2)))
print(money_left+str(20%2))