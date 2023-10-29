# Exercise 1: Variables:
#Assign a message to a variable, and print that message.
#Then change the value of the variable to a new message, and print the new
#message.
message="Enter name:"
print(message)
message="Please Enter your name:"
print(message)

# Exercise 2: Variables 
#Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks:
#Albert Einstein once said, “A person who never made a mistake never tried anything new.
 #This is the solution
name_of_the_author="Quaid-e-Azaam"
Quote="\"I assure you, \nDevided you Fall, United you Stand.\""
print(name_of_the_author, "once said, " + Quote," ")

# Exercise 3: Stripping Names :ballot_box_with_check:
#Tidy up the code to make it easier to understand
#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, “\t” and “\n”, at least once.
#Print the name once, so the whitespace around the name is displayed. 
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
#This is the solution
name="\t   Clara James    \n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


# Exercise 4: Favorite Number
#Use a variable to represent your favorite number. Then,using that variable, create a message that reveals your favorite number. Print
#that message.
#This is the solution
Favorite_Number=7
print("My favorite number is ",Favorite_Number) 


# Exercise 5: USB Shopper 
#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.
#This is the solution
USB_sticks_Bought="Total USB sticks she can buy =£"
money_left="Total pounds she will be left with =£"
print(USB_sticks_Bought+str(int(50/6)))
print(money_left+str(50%6))

