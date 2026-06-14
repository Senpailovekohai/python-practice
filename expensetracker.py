import json
import os
if os.path.exists("expenses.json"):
   with open("expenses.json","r") as file:
      expense=json.load(file)
else:
   expense=[]
   

while True:
    print("1.Add Expense" )
    print("2.Delete Expense")
    print("3. View Specifiy Expense")
    print("4.View Detail Calculation")
    print("5.Exit")
   
    choice=input("Enter your choice:")  
    if choice=="1":
        condition="yes"
        while condition =="yes":
            name=input("Enter expenses name:").lower().strip()
            while True:
                try:
                    amount=int(input("Enter amount of expense:"))
                    break
                except:
                    print("Please only Input Enter Number:")
            cost={
        "name":name,
        "amount":amount
        
            }
            expense.append(cost)
            condition=input("Do you want to add another expenses?").lower()
            while condition !="yes" and condition!="no":
                print("Please Enter Yes/No")
                condition=input("Do you want to add another expenses?").lower()

    elif choice=="2":
        delete=input("Which expense you wanna delete:").lower().strip()
        for de in expense:
          if de["name"]==delete:
             expense.remove(de)
             print("Sucessfull Deleted!!")
             break
        else:
            print("Expense Name not Found!!")

    elif choice=="3":
        exp=input("Which expense you wanna see?").lower().strip()
        for cost in expense:
           if cost["name"]==exp:
               print(
                    cost["name"],
                     "-",
                    cost["amount"]
               )
               break
        else:
           print("Expense name not found!!")
               
    
           
       
    elif choice=="4":
        total_amount=0
        for cost in expense:
            print(
          cost["name"],
          "-",
          cost["amount"]
       )
            total_amount=total_amount+cost["amount"]
        print("Your total amount is:",total_amount)
            
    elif choice=="5":
        break



   
with open("expenses.json","w") as file:
    json.dump(expense, file)