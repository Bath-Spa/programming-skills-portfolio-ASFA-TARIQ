print(42==42)
print(40==42)
print('hello'=='hello')
print('hello'=='Hello')
print('dog'!='cat')
print(42==42.0)

print(1==1.0>0.75)
print(2==2.0<1.5)
print(3<2<"2")
print(1<2<3)
print(1<2 and 2<3)
print(2+2==4 and not 2+2==5 and 2*2==2+2)
print(5>4 or 3<4 and 5>5)

grade=95
print(100>=grade>=80)

#if statement
name='Anmol'
if name=='Anmol':
 print('Hi, Anmol')

if name!="Anmol":
    print('You are not Anmol')   



#else if statement
name='Anmol'
if name=='Anmol':
    print('Hi, Anmol')
else:
    print('You are not anmol')

#elif statement
name='Anmol'
if name=='Nayab':
  print('Hi,Nayab')
elif name=='Bisma':
  print('Hi, Bisma')
else:
  print('Who are you?')



response_code = 201
match response_code:
   case 200:
     print ("OK")
   case 201:
     print("Created")
   case 300:
     print("Multiple choices")



lang=input("What's the program language you want to learn? ")
match lang:
  case "JavaScript":
    print("You can brcome a web developer.")
  case "Python":
    print("You can become a Data scientist")
  case  "PHP":
    print("You can become a backend developer")
  case "Solidity":
    print("Yiu can become a Blockchain developer")
  case "Java":    
    print("You cann become a mobile app developer")
  case _:
    print("The language doesn't matter, what matters is solving problems")




    
