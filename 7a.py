
s=input("Enter the string:")
uppercase=0
lowercase=0
for i in s:
    if(i.islower()):
        lowercase+=1
    elif(i.isupper()):
        uppercase+=1
print(uppercase," ",lowercase)