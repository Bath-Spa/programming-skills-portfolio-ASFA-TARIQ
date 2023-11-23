## Exercise 1: Names :
#Store the names of a few of your friends in a list called names.
#Print each person’s name by accessing each element in the list, one at a time.
#This is the solution
names=["Ayesha","Faghrah","Manahil","Amna","Hibba"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


## Exercise 2: Greetings :
#Start with the list you used in Exercise 1, but instead of just
#printing each person’s name, print a message to them. The text of each message should be the same, but each message should be 
#personalized with the person’s name.
# This is the solution
names =names=["Ayesha","Faghrah","Manahil","Amna","Hibba"]
message = "Hello! \n" + names[0] + ", how are you?" 
print(message)
message = "Hello! \n" + names[1] + ", how are you?" 
print(message)
message = "Hello! \n" + names[2] + ", how are you?" 
print(message)
message = "Hello! \n" + names[3] + ", how are you?" 
print(message)
message = "Hello! \n" + names[4] + ", how are you?" 
print(message)








## Exercise 3: Your Own List :
#Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
#This the solution
mode_of_transport=["Airplane","ferry","car","metro","motorcycle","Bicycle"]
print(mode_of_transport[0] + " flies high in the sky.")
print("I went to Dubai by a "+ mode_of_transport[1])
print("I'm old enough to drive a " + mode_of_transport[2] )
print("I like traveling by "+ mode_of_transport[3])
print("My cousin owns a blue "+ mode_of_transport[4])
print(mode_of_transport[5] +" is the most healthiest mode of transportation")



## Exercise 4: Guest List :
#If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d
#like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
#This is the solution
#Invite to dinner
guest=["Ayesha Abid","Hibba Abdullah","Amna Amir","Aimal Mirza","Laiba Rashid"]
print("Dear " + guest[0]+ ", I would like to invite you to dinner")
print("Dear, " + guest[1]+ " I would like to invite you to dinner")
print("Dear, " + guest[2]+ " I would like to invite you to dinner")
print("Dear, " + guest[3]+ " I would like to invite you to dinner")
print("Dear, " + guest[4]+ " I would like to invite you to dinner")


## Exercise 5: 
#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.
#This the solution
#Invite to dinner
guest=["Ayesha Abid","Hibba Abdullah","Amna Amir","Kainat Nadeem","Laiba Rashid"]
print("Dear " + guest[0]+ ", I would like to invite you to dinner")
print("Dear, " + guest[1]+ " I would like to invite you to dinner")
print("Dear, " + guest[2]+ " I would like to invite you to dinner")
print("Dear, " + guest[3]+ " I would like to invite you to dinner")
print("Dear, " + guest[4]+ " I would like to invite you to dinner")
#Amna Amir couldn't make it
guest[2]="Faghrah Sarfaraz"
#The new guest list
print("Dear " + guest[0]+ ", I would like to invite you to dinner")
print("Dear, " + guest[1]+ " I would like to invite you to dinner")
print("Dear, " + guest[2]+ " I would like to invite you to dinner")
print("Dear, " + guest[3]+ " I would like to invite you to dinner")
print("Dear, " + guest[4]+ " I would like to invite you to dinner")






## Exercise 6: Shrinking Guest List :
#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
#This is the solution
#Invite list
guest=["Ayesha Abid","Hibba Abdullah","Amna Amir","Kainat Nadeem","Laiba Rashid"]
print("\nDear, " + guest[0]+ ", I would like to invite you to dinner.")
print("Dear, " + guest[1]+ " I would like to invite you to dinner.")
print("Dear, " + guest[2]+ " I would like to invite you to dinner.")
print("Dear, " + guest[3]+ " I would like to invite you to dinner.")
print("Dear, " + guest[4]+ " I would like to invite you to dinner.")
#Amna Amir couldn't make it
guest[2]="Faghrah Sarfaraz"
#The new guest list
print("\nDear, " + guest[0] + "I would like to invite you to dinner.")
print("Dear, " + guest[1] + " I would like to invite you to dinner.")
print("Dear, " + guest[2] + " I would like to invite you to dinner.")
print("Dear, " + guest[3]  + " I would like to invite you to dinner.")
print("Dear, " + guest[4] + " I would like to invite you to dinner.")
#Sorry I can only invite two people on the list
print("\nSorry, we can only invite two people to dinner.")
print("Sorry, " + guest.pop(2) + " there is no room in the table.")
print("Sorry, " + guest.pop(0) + " there is no room in the table.")
print("Sorry, " + guest.pop(1) + " there is no room in the table.")
#inviting the other guest
print("\nDear, " + guest[0] + " I would like to invite you to dinner.")
print("Dear, " + guest[1] + " I would like to invite you to dinner.")
# Empty out the list.
del(guest[0])
del(guest[0])
#the list is empty.
print(guest)



## Exercise 7: Seeing the World :
#Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
#•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#•	 Use sorted() to print your list in alphabetical order without modifying the actual list
#•	 Show that your list is still in its original order by printing it.
#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#•	 Show that your list is still in its original order by printing it again.
#•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
#•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
#this is the solution
locations=["Maldeives","Switzerland","Venice","Turkey","Egypt","China","Korea"]
print("Locations in Original order:")
print(locations)
print("\nLocations in Alphabetical order:")
print(sorted(locations))
print("\nLOcations in Original order:")
print(locations)
print("\nLocations in Reverse alphabetical order:")
print(sorted(locations, reverse=True))
print("\nLocations in Original order:")
print(locations)
print("\nLocatons in Reversed order:")
locations.reverse()
print(locations)
print("\nLocations in Original order:")
locations.reverse()
print(locations)
print("\nLocations in Alphabetical order:")
locations.sort()
print(locations)
print("\nLocations in Reverse alphabetical order:")
locations.sort(reverse=True)
print(locations)