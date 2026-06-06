detail=[]
condition ="yes"
while condition=="yes":
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    student={
        "name":name,
        "age":age
    }
    detail.append(student)
    condition=input("Do you want to add another?").lower()
    while condition !="yes" and condition!="no":
        print("Please enter Yes/No")
        condition=input("Do you want to add another?").lower()

for info in detail:
    print ("Student Name:",info["name"],
           "| Age:",
           info["age"]
           

        )
