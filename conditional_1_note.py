p1="I not like this"
p2="click to this"
p3="link is useful not this"

massage=input("enter your comment:")

if((p1 in massage)or(p2 in massage)or(p3 in massage)):
    print("this comment is spam")

else:
    print("this comment is not spam")    
