print('Welcome To Indala College Sports Event')

a=input("Enter your Name : ")
print('Thank you')
while(1):
    b=input("Which Sports You are Looking For.? \n 1) cricket \n 2) carrom \n 3) kabbadi \n")

    if(b=="cricket"):
        print('Go to big ground')
        while(1):
            c=int(input("enter your age"))
            if(c<=20):
                print('you are in SECTION A')
                break
            else:
                print('you are in SECTION B')  
                break 
                       
    elif(b=="carrom"):
        print('Go to class no.03')
        while(1):
            c=int(input("enter your age"))
            if(c<=20):
                print('you are in SECTION C')
                break
            else:
                print('you are in SECTION D') 
                break

    elif(b=="kabbadi"):
        print('Go to small ground')
        while(1):
            c=int(input("enter your age"))
            if(c<=20):
                print('you are in SECTION E')
                break
            else:
                print('you are in SECTION D') 
                break

    else:
        print('No sports found')
    
print(f"Thank You {a} & All the best for {b}")
