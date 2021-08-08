# import random
import time as t
import datetime as dt
# import os

# Admin email - admin , password - admin

store_items = {1001:["Tandori","4 Pieces", 121],
               1002:["Biryani","250 gms", 250],
               1003:["Pizza","Medium", 350],
               1004:["Chicken Shwarama","1 Piece", 99],
               1005:["Paneer Frankie","1 Piece", 99]}
my_cart ={}


class foodpanda:
    """This is a class where you can select your favuorite dish and order it """
    def __init__(self):
        print(('*')*20,"Welcome to Food Panda !!!",('*')*20)

        self.admin = False
        self.user = False
        self.u_details = {"vin@":{"Name":"Vinay","Contact Number":1234567,"Address":"Mumbai","Password":"123"}}
        self.history = {}

    ####################################################################################################################

    def login(self):
        """This is a function where user login"""
        input1 = int(input("Select a profile to login:\nPress 1- Admin\nPress 2-Customer\nPress 3-Register from here\n=>"))
        if input1 == 1:
            email = input("Enter Email ID\n")
            password = input("Enter Password\n")
            print("Logging in...")
            t.sleep(0.5)
            if email == "admin" and password== "admin":
                print("Welcome Admin to Food Panda. What changes you would like to do??")
                self.admin = True
            else:
                print("Invalid credentials for admins")
                self.login()

        elif input1 == 2:
            email = input("Enter Email ID\n")
            password = input("Enter Password\n")
            print("Logging in...")
            t.sleep(0.5)
            if email in self.u_details and password == self.u_details[email]["Password"]:
                print(('*')*20,"Welcome to Food Panda !!!",('*')*20)
                self.user = True
            else:
                print("Wrong Credentials. Please try again")
                self.login()
        elif input1 ==3:
            self.register()

        else:
            print("Invalid Option")
            self.login()

    ####################################################################################################################

    def register(self):
        """This is function for registeration"""
        d ={}
        self.name = input("Enter your Full Name:\n")
        self.number = input("Enter your Contact Number:\n")
        self.email = input("Enter your Email Id:\n")
        self.addrs = input("Enter your Address:\n")
        self.password = input("Enter your Password\n")
        d[self.email] = {"Name":self.name,"Contact Number":self.number,"Address":self.addrs,"Password":self.password}
        print("Please wait while we register your details")
        t.sleep(1)
        print("Registration Successful")
        self.u_details.update(d)
        self.login()

    ####################################################################################################################

    def show_items(self):
        print("\n")
        print("{: >5} {: >25} {: >10} {: >10}".format("Code","Item","Quantity","Price"))
        for item in store_items:
            print("{: >5} {: >25} {: >10} {: >10}".format(item,*store_items[item]))

    ####################################################################################################################

    def order(self):
        print("Please give input as mentioned below !!!")
        x = input("Enter the Code and Quantity with space separated values you want to add to cart, e.g. 1003 2\n").split(" ")
        code = int(x[0])
        quantity = int(x[1])
        total = 0
        for foodcode in store_items:
            if foodcode == code:
                is_exist = False
                for i in my_cart:
                    if code == i:
                        is_exist= True
                        break

                total = quantity * store_items[foodcode][2]
                if is_exist:
                    my_cart[code][0] += quantity
                    my_cart[code][2] += total

                else:
                    od = {}
                    od[code]= [quantity,store_items[code][2],total]
                    my_cart.update(od)

    ####################################################################################################################

    def remove_item(self):
        input2 = input("Enter the code and quantity of item you want to remove. E.g 1001 2\n").split()
        code = int(input2[0])
        dis = int(input2[1])
        for item in my_cart:
            if item == code:
                if dis < my_cart[item][0]:
                    my_cart[item][0] = my_cart[item][0]-dis
                    my_cart[item][2] = my_cart[item][0] *store_items[item][2]
                elif dis == my_cart[item][0]:
                    my_cart.pop(item)
                break
        self.check_cart()


    def confirm(self):
        self.check_cart()
        for items in my_cart:
            self.history[items]=[*my_cart[items]]
            self.history[items].append(dt.datetime.now())
        print("'Order Placed Successfully. Delivery guy will be their in less than 30 mins or food is free'")
        print()
        for i in my_cart:
            my_cart.pop(i)

    def hist(self):
        for i in self.history:
            print(f"Date & Time: {self.history[i][3]}\nFood Id: {i}\nQuantity: {self.history[i][0]}\n"
                  f"Price: {self.history[i][1]}\nTotal: {self.history[i][2]}")
            print()


    ####################################################################################################################


    def update_profile(self):
        print("What do you want to update?\n1=> Name\n2=> Number\n3=>Addrress\n4=> Password\n5=>Back to Menu")
        input3 = int(input("Enter the number:\n"))
        for i in self.u_details:
            if self.email == i:
                if input3 == 1:
                    self.u_details[self.email]['Name'] = input("Name:\n")
                    print("Successfully Updated the Name")
                elif input3 == 2:
                    self.u_details[self.email]['Contact Number'] = input("Number:\n")
                    print("Successfully Updated the Number")
                elif input3 == 3:
                    self.u_details[self.email]['Address'] = input("Address:\n")
                    print("Successfully Updated the Address")
                elif input3 == 4:
                    self.u_details[self.email]['Password'] = input("Password:\n")
                    print("Successfully Updated the Password")
                elif input3 == 5:
                    print("Going back to Menu")
                    self.menu()
                else:
                    print("Inavlid Option")
                    break


    ####################################################################################################################

    def check_cart(self):
        print("\n----------------------------------------")
        print("{: >5} {: >10} {: >10} {: >10}".format("Item", "Qty", "Price", "Total"))

        for customer_items in my_cart:
            print("{: >5} {: >10} {: >10} {: >10}".format(customer_items,*my_cart[customer_items]))
        self.getTotalPrice()
        print("\n----------------------------------------")

    ####################################################################################################################

    def getTotalPrice(self):
        self.total_price = 0
        for customer_items in my_cart:
            self.total_price += my_cart[customer_items][2]
        print("\n{: >38}".format(f"TOTAL: {self.total_price}"))


    #******************************************   Admin Functions ******************************************************

    def remove_food(self):
        input5 = int(input("Enter the ID of Food you want to remove:\n"))
        for i in store_items:
            if i == input5:
                store_items.pop(i)
                print("Item Removed Successfully")
            else:
                print("Enter a valid Id")


    def edit_food(self):
        input6=int(input("Enter the Id of Food item you want to edit:\n"))
        for i in store_items:
            if i == input6:
                input7 = int(input("Press 1=> Name\nPress 2=> Quantity or Size\nPress 3 => Price\n=>"))
                if input7 == 1:
                    store_items[i][0] = input("Enter Food Name")
                    print("Item Updated Successfully")
                elif input7 == 1:
                    store_items[i][1] = input("Enter Quantity or Size")
                    print("Item Updated Successfully")
                elif input7 == 1:
                    store_items[i][0] = int(input("Enter Price"))
                    print("Item Updated Successfully")
            else:
                print("Enter a valid Food Id")


    def add_food(self):
        add ={}
        Name = input(("Enter the new Item Name"))
        Quantity = input("Enter the Quantity or Size of item")
        Price = int(input("Enter the Price of new Item"))
        add[max(store_items)+1] = [Name,Quantity,Price]
        store_items.update(add)
        print("Item added Successfully")


    ####################################################################################################################

    def menu(self):
        input4 = int(input("1 => Login\n2 => Register\n=>"))
        if input4 == 1:
            self.login()
        elif input4 == 2:
            self.register()
        else:
            print("Invalid Selection")
            self.menu()
        if self.user:
            print("\n\t\t\t\t\t A => Add to Cart\n\t\t\t\t\t "
                  "R => Remove item from cart\n\t\t\t\t\t "
                  "H => Order History\n\t\t\t\t\t "
                  "U => Update Profile\n\t\t\t\t\t "
                  "C => Confirm Order\n\t\t\t\t\t "
                  "E => Exit")
            ans = True
            while ans:
                try:
                    self.show_items()
                    self.check_cart()
                    print("----------------------------------------")
                    self.choice = input("Please Enter 'A'/'R'/'H'/'U'/'C'/'E' :\n").upper()
                    if self.choice == "E":
                        ans = False
                    elif self.choice == "A":
                        self.order()
                    elif self.choice == "R":
                        self.remove_item()
                    elif self.choice == "U":
                        self.update_profile()
                    elif self.choice == "C":
                        self.confirm()
                    elif self.choice == "H":
                        self.hist()
                    else:
                        self.check_cart()
                except Exception as e:
                    print(e)

        elif self.admin:
            ans = True
            while ans:
                try:
                    self.show_items()
                    print("----------------------------------------")
                    self.choice = input("Please Enter\n'A' to Add Food Item\n'R' to Remove Food Item\n'E' to Edit Food Item\n 0 to exit\n=>").upper()
                    if self.choice == "0":
                        ans = False
                    elif self.choice == "A":
                        self.add_food()
                    elif self.choice == "R":
                        self.remove_food()
                    elif self.choice == "E":
                        self.edit_food()
                    else:
                        self.check_cart()
                except Exception as e:
                    print(e)


vin = foodpanda()
vin.menu()