## Exercise 1: Person :
#Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live.
#Youshould have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
#This is solution
information={'first_name':'kinza', 'last_name':'Malik', 'age':'19', 'city':'United Arab Emirate'}
print("Information about a person")
for key, value in information.items():
    print(f"{key}: {value}")


# Exercise 2: Glossary :
#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
#their meanings as values.
#* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
#each word-meaning pair in your output.
#This is the solution
print("\nSome progmming words of python with there explanation")
programming_words={'if statement':'\"The if statement evaluates an expression, and if that expression is True then execute the following indented code\"',
                   'print function':'\"Displays output on the screen.\"',
                   'Assignment operator':'\"Assignment operatoris used to assign value to a variabl\"',
                   'List':'\"A list is an ordered set of values, where each value is identified by an index\"',
                   'Control flow': '\"Control flow is the order in which individual statements instructions, or function are executed or evaluated\"',
                 }
for key, value in programming_words.items():
    print(f"\n{key}:\n\t {value}")


## Exercise 3: Glossary 2 :
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3s (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
#This is the solution
print("\nGlossary for python with there explanation")
programming_words={'if statement':'\"The if statement evaluates an expression, and if that expression is True then execute the following indented code.\"',
                   'print function':'\"Displays output on the screen.\"',
                   'Assignment operator':'\"Assignment operatoris used to assign value to a variabl.\"',
                   'List':'\"A list is an ordered set of values, where each value is identified by an index.\"',
                   'Control flow': '\"Control flow is the order in which individual statements instructions, or function are executed or evaluated.\"',
                   'Dictionaries':'\"A dictionary is a collection of key-value pairs.\"',
                   'Boolean Operators':'\"There are there Boolean operators;and,or and not.\"',
                   'lenght of the list':'\"len() function is used to find lenght of the list.\"',
                   'reverse list':'\"reverse() function reverse the elements of the list.\"',
                   'Data structures':'\"Data structures are containers that organize and group data according to type.\"'
                 }
for key, value in programming_words.items():
    print(f"\n{key}:\n\t {value}")






# Exercise 4: Rivers :
#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#* Use a loop to print the name of each river included in the dictionary.
#* Use a loop to print the name of each country included in the dictionary.
#This is the solution
rivers={'Nile':'Egypt',
        'Amazon river':'South america',
        'Yangtze River':'China'
}
for key, value in rivers.items():
    print("The " + key + " runs through " + value + ".")
print('\nRivers')
for key in rivers.keys():
  print(key)
print('\nCountry')
for value in rivers.values():
  print(value)


# Exercise 5: Pets :
#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, 
# print everything you know about each pet
#This is the solution
pets=[]
pet={
   'Pet name': 'Jami',
   'Animals kind' : 'Cat',
   'Owners name': 'Claudia' ,
    }
pets.append(pet)

pet={
   'Pet name': 'Pesco',
   'Animals kind' : 'Dog' ,
   'Owners name': 'Ralph' ,
    }
pets.append(pet)

pet={
   'Pet name': 'Luca',
   'Animals kind' : 'Parrot' ,
   'Owners name': 'Hana' ,
   }
pets.append(pet)

pet={
   'Pet name': 'Sam',
   'Animals kind' : 'Duck' ,
   'Owners name': 'Tiana' ,
}
pets.append(pet)

pet={
   'Pet name': 'Philip',
   'Animals kind' : 'Rabbit' ,
   'Owners name': 'Sara' ,
}
pets.append(pet) 

for pet in pets:
    print("\nInformation about " + pet['Pet name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))


