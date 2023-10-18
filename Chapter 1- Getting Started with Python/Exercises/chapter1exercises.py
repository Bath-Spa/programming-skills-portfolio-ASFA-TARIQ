# Exercise 1: Print Strings :ballot_box_with_check:
#Write a Python program to print the following string in a specific format.
#Twinkle, twinkle, little star,
	#How I wonder what you are! 
		#Up above the world so high,   		
		#Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
	#How I wonder what you are
#This is the solution of exercise
line1="Twinkle, twinkle, little star,"
print(line1)
line2="	   How I wonder what you are!  "
print(line2)
line3="       Up above the world so high,"	
print(line3)   		
line4="       Like a diamond in the sky. "
print(line4)
line5="Twinkle, twinkle, little star, "
print(line5)
line6="    How I wonder what you are"
print(line6)

# Exercise 2: Print the Version of Python :ballot_box_with_check:

#Write a Python program to get the Python version you are using.
#This the solution of the exercise
import sys
print("Python version you are using:")
print (sys.version)

## Exercise 3: Print date and Time :ballot_box_with_check:
#Write a Python program to display the current date and time.
#This is the solution ofexercise
import datetime
current_date_time = datetime.datetime.now()
print("The current date and time is:",current_date_time )

## Exercise 4: Strings Concatination :ballot_box_with_check:
#Write three strings in different variables and print the output as one string.
#the solution of the exercise:
x="Here"
y="you"
z="are."
print(x, " " + y, " " + z)


## Exercise 5: Compute area of Circle :ballot_box_with_check:
#Write a Python program which accepts the radius of a circle from the user and compute the area.
#the solution of the exercise :
radius = float(input('Enter the radius of a circle whose area is required: ',))
area=3.14 * radius * radius
print("Area of circle is = ",area)



