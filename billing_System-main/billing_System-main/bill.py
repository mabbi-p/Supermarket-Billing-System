def addItem():
    itemName=input("Enter Item Name: ")
    itemPrice=int(input("Enter Item Price: "))
    itemQuant=int(input("Enter Total Quantity: "))
    items={"Name":itemName, "Price":itemPrice, "Quant":itemQuant}
    store.append(items)
    print()
    print("Item Added Successfuly!")
    
def bill():
    userItem=input("Enter Selling Item: ")
    userQuant=int(input("Enter Quantity: "))
    isFound=False
    for i in store:
        if userItem==i["Name"] and userQuant <=i["Quant"]:
            isFound=True
            i["Quant"]=i["Quant"]-userQuant
            print("Remaining Quantity: ",i["Quant"])
            totalBill=i["Price"]*userQuant
            print("Total Bill: ",totalBill)
            break
            
    if isFound==False:
        print() 
        print("Item not available!")
        
    
store=[]
while True:
    print("1.Add Items")
    print("2.Print Bill")
    print("3.Exit")
    choice=int(input("Enter Choice: "))
    print()
    
    if choice==1:
        print()
        addItem()
        print()
    elif choice==2:
        print()
        bill()
        print()
    elif choice==3:
        print()   
        print("Good Bye!") 
        break
        print()
    else:
        print()
        print("Invalid Input!")
        print()
        