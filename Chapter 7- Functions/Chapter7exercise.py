# Exercise 1:   Message  :
#Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the
#function, and make sure the message displays correctly.
#This is the solution
def display_message():
    print("\nIn this chapter I'm learning about functions")

display_message()

# Exercise 2: Favorite Book :
#Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my
#favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
#This is the solution
def favorite_book(fname):
    print("\nOne of my favorite book is " + fname+ ".")
favorite_book("Divergent")    



# Exercise 3: T-Shirt  :
#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
#arguments to make a shirt. Call the function a second time using keyword arguments.
#This is the solution
def make_shirt(size,message):
    print("\nI want a " + size + " t-shirt")
    print("The text printed on the t-shirt will be " + message + ".")
make_shirt("Small", "Hello World!")
make_shirt(size="Large", message="Good Day")

# Exercise 4:  Large Shirts :black
#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different message.
#This is the solution
def make_shirt(size="Large" , message="I Love Python"):
    print("\nI want a " + size + " t-shirt.")
    print("The text printed on the t-shirt will be " + message + " .")
make_shirt()
make_shirt(size="medium")
make_shirt("small", "Be Positive")

# Exercise 5: Cities:
#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
#such as Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.
#This is the solution
def describe_city(name_of_city, name_of_country="Germany"):
    print(name_of_city + " is in " + name_of_country+ ".")
describe_city("\nBerlin")
describe_city("Venice", "Italy")
describe_city("Hamburg")