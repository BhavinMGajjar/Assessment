
fruits = {'Fruit':'Apple','Quantity':5,'Price':70}

def perform_more():

    opp = str(input("Do you want to perform more operation? "))
    if opp=='y':
         manager_choice()
    else:
        print("Thank you for visiting the Fruit store, Good bye")

def add_fruit():

            f_name = str(input("Enter Fruit Name : "))
            qty = int(input("Enter Quantity : "))
            price = int(input("Enter price : "))
            fruits["Fruit"] = f_name
            fruits["Quantity"] = qty
            fruits["Price"] = price}
            perform_more()

def update_fruit():

            f_name = str(input("Enter Fruit Name : "))
            qty = int(input("Enter Quantity : "))
            price = int(input("Enter price : "))
            fruits.update({"Fruit":f_name})
            fruits.update({"Quantity":qty})
            fruits.update({"Price":price})
            perform_more()



def show_fruit():

           print(fruits)
           perform_more()


def manager_choice():
            print("1) Add Fruit stock")
            print("2) Show Fruit stock")
            print("3) Update Fruit stock")
            manage_choice = int(input("Enter your choice : "))
            if manage_choice==1:
               add_fruit()
            elif manage_choice==2:
                show_fruit()
            elif manage_choice==3:
                update_fruit()

print("Welcome to Fruit store")
print("1) Manager")
print("2) Customer")

role_num = int(input("Select your role : "))
dist = {1:'Manager',2:'Customer'}
#print(dist[1])

for i in dist:
    if i==role_num:
        print("Fruit Market "+ dist[i])
        if role_num==1:
            manager_choice()





