#Vending Machine program
print("__________________________________________________________________________________________________________________________________")  
print("\033[1m                                  ***WELCOME TO SNACKS AND DRINKS VENDING MACHINE***\033[0m")
print("__________________________________________________________________________________________________________________________________")  
print("All items in this vending machine are exclusive of vat 5%")
Chips= {
      'Doritos': 'Code A'  ,'Cheetos': 'Code B', 'Takis': 'Code C' ,'Lays forno': 'Code D',
    }
Chocolates= {
       'Galaxy': 'Code E', 'Herseys': 'Code F','Dairymilk': 'Code G','Twix': 'Code H',
    }
Cookies= {
        'Choco chip cookies': 'Code I','Butter cookies': 'Code J','Peanut cookies': 'Code K','Oreo': 'Code l',
    }
#Displaying Snacks
print("\n\033[1mChips:\033[0m")  
for keys, values in Chips.items():
    print(f"\n{keys}:\n\t{values}")
print("\n\033[1mChocolates:\033[0m")     
for keys, values in Chocolates.items():
    print(f"\n{keys}:\n \t{values}")
print("\n\033[1mCookies:\033[0m")     
for keys, values in Cookies.items():
    print(f"\n{keys}:\n \t {values}")

#Drinks 
Juices={ 
    'Orange juice': 'Code 01', 'Apple juice': 'Code 02', 'Mango juice': 'Code 03','Cocktail juice': 'Code 04',
       }
Cold_Drinks={
    'Pepsi': 'Code 05', 'Mountain Dew': 'Code 06','Fanta': 'Code 07' ,'sprite': 'Code 08'
            }
Other_Drinks={
    'Normal water': 'Code 09','Cold water': 'Code 10','Ice tea': 'Code 11','Cold coffee': 'Code 12',
             }
#Displaying Drinks 
print("\n\033[1mJuices:\033[0m")  
for keys, values in Juices.items():
    print(f"\n{keys}:\n\t{values}")
print("\n\033[1mCold Drinks:\033[0m")     
for keys, values in Cold_Drinks.items():
    print(f"\n{keys}:\n \t{values}")
print("\n\033[1mOther Drinks:\033[0m")     
for keys, values in Other_Drinks.items():
    print(f"\n{keys}:\n \t {values}")
#Snacks 
Chips= {     
        'Code A' : {'Name':'Doritos','Price': '4.00 ','Stock':'8'},
        'Code B' : {'Name':'Cheetos','Price': '5.00 ','Stock':'8'},
        'Code C' : {'Name':'Takis','Price': '8.00 ','Stock':'8'},
        'Code D' : {'Name':'Lays forno','Price': '4.00 ','Stock':'8'}
       } 

Chocolates= { 
                'Code E' : {'Name':'Galaxy','Price': '5.00 ','Stock':'8'},
                'Code F' : {'Name':'Herseys','Price': '6.00 ','Stock':'8'},
                'Code G' : {'Name':'Dairymilk','Price': '4.00 ','Stock':'8'},
                'Code H' : {'Name':'Twix','Price': '5.00 ','Stock':'8'}
            }    
Cookies= {
            'Code I' : {'Name':'Choco chip cookies','Price': '8.00 ','Stock':'8'},
            'Code J' : {'Name':'Butter cookies','Price': '6.00 ','Stock':'8'},
            'Code K' : {'Name':'Peanut cookies','Price': '7.00 ','Stock':'8'},
            'Code L' : {'Name':'Oreo','Price': '5.00 ','Stock':'12'}               
         }  
#Drinks
Juices={
            'Code 01' : {'Name':'Orange juice','Price': '3.00 ','Stock':'8'},
            'Code 02' : {'Name':'Apple juice','Price': '3.00 ','Stock':'8'},
            'Code 03' : {'Name':'Mango juice','Price': '3.00 ','Stock':'8'},
            'Code 04' : {'Name':'Cocktail','Price': '3.00 ','Stock':'8'},
        }   
Cold_Drinks={
                'Code 05' : {'Name':'Pepsi','Price': '5.00 ','Stock':'8'},
                'Code 06' : {'Name':'Mountain Dew','Price': '5.00 ','Stock':'8'},
                'Code 07' : {'Name':'Fanta','Price': '5.00 ','Stock':'8'},
                'Code 08' : {'Name':'Sprite','Price': '5.00 ','Stock':'8'},
            }
Other_Drinks={
                'Code 09' : {'Name':'Normal water','Price': '2.00 ','Stock':'8'},
                'Code 10' : {'Name':'Cold water','Price': '3.00 ','Stock':'8'},
                'Code 11' : {'Name':'Ice tea','Price': '5.00 ','Stock':'8'},
                'Code 12' : {'Name':'Cold coffee','Price': '6.00 ','Stock':'8'},
            }
print("__________________________________________________________________________________________________________________________________")   
# ask user for input
while True:
    Product_Code = input("Enter the product code whose details you want to know Enter Done if you are one with checking the product detail and want to order\n this will show the products name, code, price and available stock (Note Please enter the exact code): ")
    if Product_Code=='Done':
        break
# check if the product code exists
    elif Product_Code in Chips:
# display Chips details
        print(f"Product Name: {Chips[Product_Code]['Name']}")
        print(f"Product Price: AED  {Chips[Product_Code]['Price']}")
        print(f"Product Stock: {Chips[Product_Code]['Stock']}")
        print("__________________________________________________________________________________________________________________________________")  

    elif Product_Code in Chocolates:
# display Chocolate details
        print(f"Product Name: {Chocolates[Product_Code]['Name']}")
        print(f"Product Price: AED {Chocolates[Product_Code]['Price']}")
        print(f"Product Stock: {Chocolates[Product_Code]['Stock']}") 
        print("__________________________________________________________________________________________________________________________________")     

    elif Product_Code in Cookies:
# display Cookies details
        print(f"Product Name: {Cookies[Product_Code]['Name']}")
        print(f"Product Price: AED {Cookies[Product_Code]['Price']}")
        print(f"Product Stock: {Cookies[Product_Code]['Stock']}") 
        print("__________________________________________________________________________________________________________________________________")  

    elif Product_Code in Juices:
# display Juices details
        print(f"Product Name: {Juices[Product_Code]['Name']}")
        print(f"Product Price{Juices[Product_Code]['Price']}")
        print(f"Product Stock: {Juices[Product_Code]['Stock']}") 
        print("__________________________________________________________________________________________________________________________________")  

    elif Product_Code in Cold_Drinks:
# display Cold Drinks details
        print(f"Product Name: {Cold_Drinks[Product_Code]['Name']}")
        print(f"Product Price: AED {Cold_Drinks[Product_Code]['Price']}")
        print(f"Product Stock: {Cold_Drinks[Product_Code]['Stock']}") 
        print("__________________________________________________________________________________________________________________________________")  

    elif Product_Code in Other_Drinks:
# display Other Drinks details
        print(f"Product Name: {Other_Drinks[Product_Code]['Name']}")
        print(f"Product Price: AED {Other_Drinks[Product_Code]['Price']}")
        print(f"Product Stock: {Other_Drinks[Product_Code]['Stock']}") 
        print("__________________________________________________________________________________________________________________________________")   

    else:
        print("Product code not found.")

#Initializing Grand_Total to 0 so in further code it can be appended
Grand_Total = 0.0
Dispensed_Items = []    

#Creating function to display the products name with there Quantities that have been dispensed
def display_dispensed_products(Dispensed_Items):
    for item in Dispensed_Items:
        print(f"{item['Quantity']} {item['Name']} have been dispensed.")

while True:
    Product_Code = input("\nEnter the product code you want to purchase Enter Done if you are done purchasing: ")
    if Product_Code=='Done':
        break

# check if the product code exists
    elif Product_Code in Chips:
# display Chips details
        print(f"Product Name: {Chips[Product_Code]['Name']}")
        print(f"Product Price: AED {Chips[Product_Code]['Price']}")
        print(f"Product Stock: {Chips[Product_Code]['Stock']}")
        Price = float(Chips[Product_Code]['Price'])
        Stock = int(Chips[Product_Code]['Stock'])
        Quantity = int(input(f"Enter the quantity of {Chips[Product_Code]['Name']} you want to buy: "))
# check if quantity is valid
        if Quantity > 0 and Quantity <= Stock:
            Total_Amount = Quantity * Price
            print(f"Your total purchase for {Chips[Product_Code]['Name']} exclusive of vat 5% will be {Total_Amount }.")
            Total_Amount_With_Vat = Total_Amount + (Total_Amount * 0.05)
            print(f"Your total purchase for {Chips[Product_Code]['Name']} inclusive of vat 5% will be {Total_Amount_With_Vat}.")
            Grand_Total += Total_Amount_With_Vat
            print("__________________________________________________________________________________________________________________________________")  
#Appending Dispensed_Items
            Dispensed_Items.append({
                'Name': Chips[Product_Code]['Name'],
                'Quantity': Quantity
            })
        else:    
            print(f"Purchase unsuccessful. Please enter a valid quantity. We only have {Chips[Product_Code]['Stock']} in stock.")

    elif Product_Code in Chocolates:
# display Chips details
        print(f"Product Name: {Chocolates[Product_Code]['Name']}")
        print(f"Product Price: AED {Chocolates[Product_Code]['Price']}")
        print(f"Product Stock: {Chocolates[Product_Code]['Stock']}")
        Price = float(Chocolates[Product_Code]['Price'])
        Stock = int(Chocolates[Product_Code]['Stock'])
#Ask user to enter the quantity of the product they want to purchase
        Quantity = int(input(f"Enter the quantity of {Chocolates[Product_Code]['Name']} you want to buy: "))
        # check if quantity is valid
        if Quantity > 0 and Quantity <= Stock:
            print("Purchased successfuly!")
            Total_Amount = Quantity * Price
            print(f"Your total purchase for {Chocolates[Product_Code]['Name']} exclusive of vat 5% will be {Total_Amount }.")
            Total_Amount_With_Vat = Total_Amount + (Total_Amount * 0.05)
            print(f"Your total purchase for {Chocolates[Product_Code]['Name']} inclusive of vat 5% will be {Total_Amount_With_Vat}. ")
            Grand_Total += Total_Amount_With_Vat
            print("__________________________________________________________________________________________________________________________________")   
#Appending Dispensed_Items            
            Dispensed_Items.append({
                'Name': Chocolates[Product_Code]['Name'],
                'Quantity': Quantity
            })

        else:
            print(f"Purchase unsuccessful. Please enter a valid quantity. We only have {Chocolates[Product_Code]['Stock']} in stock.")

    elif Product_Code in Cookies:
# display Chips details
        print(f"Product Name: {Cookies[Product_Code]['Name']}")
        print(f"Product Price: AED {Cookies[Product_Code]['Price']}")
        print(f"Product Stock: {Cookies[Product_Code]['Stock']}")
        Price = float(Cookies[Product_Code]['Price'])
        Stock = int(Cookies[Product_Code]['Stock'])
#Ask user to enter the quantity of the product they want to purchase
        Quantity = int(input(f"Enter the quantity of {Cookies[Product_Code]['Name']} you want to buy: "))
# check if quantity is valid
        if Quantity > 0 and Quantity <= Stock:
            Total_Amount = Quantity * Price
            print(f"Your total purchase for {Cookies[Product_Code]['Name']} exclusive of vat 5% will be {Total_Amount }.")
            Total_Amount_With_Vat = Total_Amount + (Total_Amount * 0.05)
            print(f"Your total purchase for {Cookies[Product_Code]['Name']} inclusive of vat 5% will be {Total_Amount_With_Vat}. ")
            Grand_Total += Total_Amount_With_Vat
            print("__________________________________________________________________________________________________________________________________")  
#Appending Dispensed_Items           
            Dispensed_Items.append({
                'Name': Cookies[Product_Code]['Name'],
                'Quantity': Quantity
            })
        else:
            print(f"Purchase unsuccessful. Please enter a valid quantity. We only have {Cookies[Product_Code]['Stock']} in stock")

    elif Product_Code in Juices:
# display Chips details
        print(f"Product Name: {Juices[Product_Code]['Name']}")
        print(f"Product Price: AED {Juices[Product_Code]['Price']}")
        print(f"Product Stock: {Juices[Product_Code]['Stock']}")
        Price = float(Juices[Product_Code]['Price'])
        Stock = int(Juices[Product_Code]['Stock'])
#Ask user to enter the quantity of the product they want to purchase
        Quantity = int(input(f"Enter the quantity of {Juices[Product_Code]['Name']} you want to buy: "))
# check if quantity is valid
        if Quantity > 0 and Quantity <= Stock:
            Total_Amount = Quantity * Price
            print(f"Your total purchase for {Juices[Product_Code]['Name']} exclusive of vat 5% will be {Total_Amount }.")
            Total_Amount_With_Vat = Total_Amount + (Total_Amount * 0.05)
            print(f"Your total purchase for {Juices[Product_Code]['Name']} inclusive of vat 5% will be {Total_Amount_With_Vat}. ")
            Grand_Total += Total_Amount_With_Vat
            print("__________________________________________________________________________________________________________________________________")   
#Appending Dispensed_Items            
            Dispensed_Items.append({
                'Name': Juices[Product_Code]['Name'],
                'Quantity': Quantity
            })
        else:
            print(f"Purchase unsuccessful. Please enter a valid quantity. We only have {Juices[Product_Code]['Stock']} in stock")

    elif Product_Code in Cold_Drinks:
# display Chips details
        print(f"Product Name: {Cold_Drinks[Product_Code]['Name']}")
        print(f"Product Price: AED {Cold_Drinks[Product_Code]['Price']}")
        print(f"Product Stock: {Cold_Drinks[Product_Code]['Stock']}")
        Price = float(Cold_Drinks[Product_Code]['Price'])
        Stock = int(Cold_Drinks[Product_Code]['Stock'])
#Ask user to enter the quantity of the product they want to purchase
        Quantity = int(input(f"Enter the quantity of {Cold_Drinks[Product_Code]['Name']} you want to buy: "))
# check if quantity is valid
        if Quantity > 0 and Quantity <= Stock:
            Total_Amount = Quantity * Price
            print(f"Your total purchase for {Cold_Drinks[Product_Code]['Name']} exclusive of vat 5% will be {Total_Amount }.")
            Total_Amount_With_Vat = Total_Amount + (Total_Amount * 0.05)
            print(f"Your total purchase for {Cold_Drinks[Product_Code]['Name']} inclusive of vat 5% will be {Total_Amount_With_Vat}. ")
            Grand_Total += Total_Amount_With_Vat
            print("__________________________________________________________________________________________________________________________________")   
#Appending Dispensed_Items            
            Dispensed_Items.append({
                'Name': Cold_Drinks[Product_Code]['Name'],
                'Quantity': Quantity
            })
        else:
            print(f"Purchase unsuccessful. Please enter a valid quantity. We only have {Cold_Drinks[Product_Code]['Stock']} in stock")

    elif Product_Code in Other_Drinks:
# display Chips details
        print(f"Product Name: {Other_Drinks[Product_Code]['Name']}")
        print(f"Product Price: AED {Other_Drinks[Product_Code]['Price']}")
        print(f"Product Stock: {Other_Drinks[Product_Code]['Stock']}")
        Price = float(Other_Drinks[Product_Code]['Price'])
        Stock = int(Other_Drinks[Product_Code]['Stock'])
#Ask user to enter the quantity of the product they want to purchase
        Quantity = int(input(f"Enter the quantity of {Other_Drinks[Product_Code]['Name']} you want to buy: "))
# check if quantity is valid
        if Quantity > 0 and Quantity <= Stock:
            Total_Amount = Quantity * Price
            print(f"Your total purchase for {Other_Drinks[Product_Code]['Name']} exclusive of vat 5% will be {Total_Amount }.")
            Total_Amount_With_Vat = Total_Amount + (Total_Amount * 0.05)
            print(f"Your total purchase for {Other_Drinks[Product_Code]['Name']} inclusive of vat 5% will be {Total_Amount_With_Vat}. ")
            Grand_Total += Total_Amount_With_Vat
            print("__________________________________________________________________________________________________________________________________")  
#Appending Dispensed_Items           
            Dispensed_Items.append({
                'Name': Other_Drinks[Product_Code]['Name'],
                'Quantity': Quantity
            })
        else:
            print(f"Purchase unsuccessful. Please enter a valid quantity. We only have {Other_Drinks[Product_Code]['Stock']} in Stock ")
    else:
        print("\nThe product code you have entered does not exist. Try entering code correctly")
#Total amount of all the product combined
print(f"\nYour grand total with vat 5% for all products is: {Grand_Total}")

#Displays users types of cards that are accepted in the vending machine    
Card_Accepted=["Visa Card","Master Card","American Express"]
print("__________________________________________________________________________________________________________________________________")  
print("\n\033[1mCard Accepted\033[0m")
print("==================================================================================================================================") 
print (Card_Accepted[0])
print (Card_Accepted[1])
print (Card_Accepted[2]) 
print("==================================================================================================================================") 
#Ask the user how would they like to pay 
print("\nHow would You  like to pay")
print("By Cash enter \033[1m\"Cash\"\033[0m")  
print("By Card enter \033[1m\"Card\"\033[0m")
print("If you want to cancel the order enter \033[1m\"Cancel\"\033[0m")
Payment_Method=input("Now enter your Payment method: ")
#If the user chooses Cash   
if Payment_Method == 'Cash':
        Amount_Paid=float(input("\nInsert the cash: ")) 
#If the amount inserted is less than the amount required         
        while Amount_Paid < Grand_Total:
            print(f"The amount You have entered is less than the amount required. ")
            Amount_Inserted = float(input("\nInsert the cash: "))
            Amount_Paid += Amount_Inserted
        if Amount_Paid > Grand_Total:
            Change = Amount_Paid - Grand_Total
        else:
            print("Payment successfully made")  
                       
#If the amount inserted is more than the amount required             
        while Amount_Paid > Grand_Total:     
            print("\nThe amount you have inserted is more than the amount required.")     
            Excess_Amount = Amount_Paid-Grand_Total
            print("\nHere is your change: {Excess_Amount} AED".format(Excess_Amount=Excess_Amount))
            print("Payment Sucessfully made")
            break
#If the amount is just perfect            
        while Amount_Paid == Grand_Total:   
            print("\n You have inserted the exact amount.")
            print("Payment Sucessfully made")
            break
#If user chooses card            
elif Payment_Method == 'Card':
    Swap_Card=input("\nSwap your card: ")
    if Swap_Card == 'Visa Card':    #Chooses Visa Card
            print("\nYou have swapped Visa card.")
    elif Swap_Card == 'Master Card':    #Chooses Master Card 
            print("\nYou have swapped Master Card.")
    elif Swap_Card == 'American Express':   #Chooses American Express
            print("\nYou have swapped American Express.")
#If the card the user have swapped does not match any of the card listed above             
    else:
            print("\nThe card you have swapped is not accepted in our vending machine.")  
#If the user cancels the order            
else :
    print("\nYou have canceled the order")

print("__________________________________________________________________________________________________________________________________")  
print("\n\033[1mitems dispensed.\033[0m")
print("==================================================================================================================================")  
# Displaying dispensed items
display_dispensed_products(Dispensed_Items)
print("==================================================================================================================================") 
print("\n\033[1mThank You For Using Our Vending Machine.\033[0m")  
print("\n\033[1mPlease come again.\033[0m")   