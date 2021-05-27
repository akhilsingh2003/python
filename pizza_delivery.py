A_id = "admin123"
A_password = "ad1234"
C_id = "cust1234"
C_password = "c1234"
stock={"pizza": 20 , "cold_drink" : 40 , "Burger" : 45 , "chocalate" : 50 , "Amul_cool": 55}
menu = "pizza\ncold_drink\nBurger\nchocalate\nAmul_cool"

while (True):
    login=int(input("Enter 1 for admin :\nEnter 2 for customer\nEnter 3 for exit \n : "))

    if login == 1:
        print("welcome in admin section " )
        id = input("id : ")
        password = input("possword : ")
        if id == A_id and password ==  A_password: 
            while (True):
                choice = input("Enter 'View' to see stocks:\n Enter 'Manage' to manage stock:\n Enter the 'Logout' to logout of account :\n ").capitalize()
                if choice == "View":
                    print("this stock is available \n")
                    print(stock)
                elif choice == "Manage":
                    print("*****welcome to manage section *****")
                    change = {}
                    for i in range(int(input("how many item change : "))):
                        v=input("enter the item ").split(':') 
                        stock[v[0]]=eval(v[1])
                    stock.update(change)
                    print(stock)
                elif choice == "Logout" :
                    print("You have succesfully logged out ")  
                    break
                else:
                    print("\t\t\n Worng choice ")
        else:
            ("Worng id or password ")            
    elif login == 2:
        print("Welcome the customer section ")
        id = input("id : ")
        password = input("password : ")
        if id == C_id and password == C_password :
            while (True):
                choice = input("Enter 'Order' for order \n Enter 'Logout' for logout \n ").capitalize()
                if choice == "Order":
                    print("available itmes are  :  \n",menu)
                    order = input("order for : ")
                    print("your order is successful for",order)
                elif choice == "Logout":
                    print("You have been sucessfully logged out ")
                    break
    elif login == 3:
        print("thanks for visit")
        break