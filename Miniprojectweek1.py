from typing import Counter

#def menu():
#    print("[1] Food Menu")
#    print("[0] Exit")

#menu()
#option = int(input("Enter your option"))

#while option != 0:
#    if option == 1:
#        pass

#    elif option == 2:
#        pass

#    else:
#        print("Invalid option.")

food =["Chocolate","Drink","Sandwich","Burger","Fries","Full English"]
prices =[1,2,6,8,3,12]

myorderfood=[]
myordercost=[]
Counter=0
total=0

print ("Welcome to the K Bar")


order = input("Can I take your order?")
if order =="No":
    nextorder = False
    print('The app has exited')
else:
    nextorder = True
    print ("Thank you")

while nextorder==True:
    foodorder = input("Please enter item")
    if foodorder =="Chocolate":
        myorderfood.append(food[0])
        myordercost.append(prices[0])
        Counter=Counter+1
        total=total+(prices[0])

    elif foodorder=="Drink":
        myorderfood.append(food[1])
        myordercost.append(prices[1])
        Counter=Counter+1
        total=total+(prices[1])

    elif foodorder=="Sandwich":
        myorderfood.append(food[2])
        myordercost.append(prices[2])
        Counter=Counter+1
        total=total+(prices[2])

    elif foodorder=="Burger":
        myorderfood.append(food[3])
        myordercost.append(prices[3])
        Counter=Counter+1
        total=total+(prices[3])

    elif foodorder=="Fries":
        myorderfood.append(food[4])
        myordercost.append(prices[4])
        Counter=Counter+1
        total=total+(prices[4])

    elif foodorder=="Full English":
        myorderfood.append(food[5])
        myordercost.append(prices[5])
        Counter=Counter+1
        total=total+(prices[5])

    else:
        print ("This item is not on the menu")
    finished = input("Have you finished ordering Y/N")
    if finished =="N":
        nextorder=True
    else:
        nextorder=False

y=0

print ("Here is your order")
print ("       ")
print ("********")
while y <Counter:

    print ("Item:"+ (myorderfood[y]))
    print ("Cost: $"+str(myordercost[y]))
    y=y+1
print ("The final cost is $"+str(total))