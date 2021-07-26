foodmenu = []
couriers = []

with open('c:/Users/Flore/Documents/GenUK-DE/foodmenu.txt', 'r') as foodmenu_file:
    for item in foodmenu_file.readlines():
        foodmenu.append(item.replace('\n', ''))

with open('c:/Users/Flore/Documents/GenUK-DE/courier.txt', 'r') as courier_file:
    for item in courier_file.readlines():
        couriers.append(item.replace('\n', ''))

print("Welcome to The K Bar")

def main_menu():
    print("[1] Food Menu")
    print("[2] Couriers List")
    print("[0] Exit this app. ")

    option = int(input("Enter you option: "))


    if option == 1:
        food_main_menu()
    elif option == 2:
        couriers_main_menu()
    elif option == 0:
        print("This app has exited")
        print("Thanks for visiting The K Bar. Goodbye!")
        exit()
    else:
        print("Invalid Input, Please try again.")


def food_main_menu():
    print("***Product Menu Options***")
    print("[0] Return to Main Menu")
    print("[1] Product List")
    print("[2] Add Product")
    print("[3] Update Product List")
    print("[4] Delete Product")

    second_option = int(input("Enter you option: "))

    if second_option == 0:
        main_menu()
    elif second_option == 1:
        print(foodmenu)
    elif second_option == 2:
        food_main_menu_add = input("Please enter in an item you would like to add : ")
        foodmenu.append(food_main_menu_add)
        with open('foodmenu.txt', 'w') as f:
            f.write(food_main_menu)
        print(foodmenu)
    # elif second_option == 3:
    #     food_main_menu_add = input("Please enter in the name of the item you would like to update: ")
    #     foodmenu.remove(food_main_menu_add)
    #     print(foodmenu)
    # elif second_option == 4:
    #     food_main_menu_add = input("Please enter in an item you would like to delete: ")
    #     foodmenu.remove(food_main_menu_add)
    #     print(foodmenu)

def couriers_main_menu():
    print("***Couriers List***")
    print("[0] Return to Main Menu")
    print("[1] Couriers List")
    print("[2] Add New Courier to List")
    print("[3] Update Couriers List")
    print("[4] Delete Courier")

    courier_option = int(input("Enter you option: "))

    if courier_option == 0:
        main_menu()
    elif courier_option == 1:
        print(couriers)
    elif courier_option == 2:
        couriers_main_menu = input("Please enter in a new courier name : ")
        couriers.append(couriers_main_menu)
        print(couriers)
    # elif courier_option == 3:
    #     couriers_main_menu = input("Please enter in the name of the courier you would like to update: ")
    #     couriers.remove(couriers_main_menu)
    #     print(couriers)
    # elif courier_option == 4:
    #     couriers_main_menu = input("Please enter in the name of the courier you would like to delete: ")
    #     couriers.remove(couriers_main_menu)
    #     print(couriers)

print()
main_menu()