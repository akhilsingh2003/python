A_id = "admin123"
A_password = "ad1234"
u_id = "user1234"
u_password = "u1234"
filename = open()
while (True):
    login=int(input("Enter 1 for admin :\nEnter 2 for user\nEnter 3 for exit \n : "))

    if login == 1:
        print("welcome in admin section " )
        id = input("id : ")
        password = input("possword : ")
        if id == A_id and password ==  A_password: 
            while (True):
                choice = input("Enter 'Read' to read blog:\n Enter 'publish' to publish the blog:\n Enter 'Delete' to delete the blog\n Enter the 'Logout' to logout of account :\n ").capitalize()
                if choice == "Read":
                    while(True):

                        print("these blogs  are available \n")
                        print(read)
                        escview = int(input("enter 0 for go back "))
                        if escview==0:
                            break