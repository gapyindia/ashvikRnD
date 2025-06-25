a=int(input("enter_your_age:"))
#statement1
if(a%2==0):
    print("a is even")
   

#statement2
if(a>=18):
    print("your are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering a negative age")

elif(a==0):
    print("you are entering 0 which is not a age")

else:
    print("you are below the age of consent")

print("end of program")    