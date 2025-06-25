mark1=int(input("enter mark 1:"))
mark2=int(input("enter mark 2:"))
mark3=int(input("enter mark 3:"))
#check the total percentage
total_percentage=(100*(mark1+mark2+mark3))/300

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("you are passed:",total_percentage)

else:
    print("you failed,try next year!:",total_percentage)    