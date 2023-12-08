#Exercise 1: Pizza Toppings :
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.
#This is the  solution
prompt = "\nEnter your desired pizza toppings:"
prompt += "\nIf done addding your toppings type quite: \n"
while True:
    Pizza_Toppings=input(prompt)
    if Pizza_Toppings != "quit":
        print("I'll add " , Pizza_Toppings , " to your pizza")
    else:
        break    


#Exercise 2: Movie Tickets: :
#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
#age, and then tell them the cost of their movie ticket
#This is the solution
prompt = "\nWhat is your age:"
prompt += "\nEnter E if you are done buying tickets \n"

while True:
    age = input(prompt)
    if age == 'E':
        break
    age = int(age)

    if age < 3:
        print("You are free")
    elif age < 13:
        print("Your ticket price will be $10")
    else:
        print("Your ticket price will be $15")

#Exercise 3: Infinity :
#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
#This is the solution
while True:
    Subject= input("What is your favourite subject:\n")


#Exercise 4: Deli :
#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
#This is the solution
sandwich_orders = ['Chicken', 'Beef', 'Cheese and Veggie', 'Grilled', 'Club']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

#Exercise 5: No Pastrami :
#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop
#to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
#This is the solution
Sandwich_Orders = ['Chicken','Pastrami', 'Beef','Pastrami' ,'Cheese and Veggie','Pastrami', 'Grilled', 'Pastrami','Club'
    ]
Finished_Sandwiches = []

print("I'm sorry but today we are out of Pastrami sandwich")
while 'Pastrami' in Sandwich_Orders:
    Sandwich_Orders.remove('Pastrami')

print("\n")
while Sandwich_Orders:
    Current_Sandwich = Sandwich_Orders.pop()
    print("I'm currently working on your " + Current_Sandwich + " sandwich.")
    Finished_Sandwiches.append(Current_Sandwich)

print("\n")
for Sandwich in Finished_Sandwiches:
    print("I made a " + Sandwich + " sandwich.")