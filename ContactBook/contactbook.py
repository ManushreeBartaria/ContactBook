ch1=1
while(ch1==1):
    ch=int(input("Do you wanna search or add a contact? press 1 for search and 2 to add"))
    if(ch==1):
        name=input("Enter name to be searched")
        with open ("contacts",'r') as f:
            listofcontacts=f.readlines()
            found=0
            for i in listofcontacts:
                if(i.startswith(name)):
                    print("The information is ",i)
                    found=1
            if(found==0):
                print("Sorry not found")

    if(ch==2):
        name=input("Enter the Name")
        number=input("Enter the number")
        info=name+" "+number+'\n'
        with open ("contacts",'a') as f:
            f.write(info)

    ch1=int(input("For more enter 1 else 0"))


