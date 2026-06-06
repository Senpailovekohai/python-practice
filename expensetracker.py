expense=[]
condition="yes"
totalamount=0
while condition =="yes":
    name=input("Enter expenses name:")
    amount=int(input("Enter amount of expense:"))
    cost={
        "name":name,
        "amount":amount
        
    }
    expense.append(cost)
    condition=input("Do you want to add another expenses?").lower()
    totalamount=totalamount+amount
    
print("Your total amount is:",totalamount)


for expenses in expense:
  print( expenses["name"],
        "-",
        expenses["amount"]
       
      
      
  )


file=open("expenses.txt","w")

for item in expense:
   file.write(
      item["name"]
      +"-"
      +str(item["amount"])
      +"won\n"
   )
file.write("Total-"+str(totalamount)+"won")
file.close()