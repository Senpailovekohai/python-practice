import json
import os
if os.path.exists("workout.json"):
    with open("workout.json","r") as file:
        day1 = json.load(file)
else:
    day1=[]

while True:
    print("1. Add exercise")
    print("2. Delete exercise")
    print("3. View speific day")
    print("4. View all")
    print("5. Summary")
    print("6. Exit")
    
    choice= input("Enter your choice:")
    if choice=="1":
        condition="yes"
        while condition == "yes":
            exercise=input("Enter your exercise:")
            while True:
                try:
                    sets=int(input("Enter the number of sets:"))
                    break
                except:
                    print("Please only input number")
            while True:
                try:
                    reps=int(input("Enter your number of reps:"))
                    break
                except:
                    print("Please only put number")
            day=input("Enter which day is it for?").lower().strip()
            workout ={
                 "exercise":exercise,
                "sets":sets,
                "reps":reps,
                "day":day
             
        }
 
            day1.append(workout)
            condition = input("Do you wanna add another?").lower()
            while condition!="yes" and condition!="no":
                print("Please Type Yes/No")
                condition = input("Do you wanna add another?").lower()
    elif choice=="2":
            
                user_input=input("Which exercise you wanna delete?")
                for workout in day1:
                    if workout["exercise"]==user_input:
                        day1.remove(workout)
                        print("Sucessfully Deleted!!")
                        break
           
    elif choice=="3":
        day=input("Which day exercise you wanna see?").lower()
        for workout in day1:
            if workout["day"]==day:
                print(workout["exercise"],
               "-",
               workout["sets"],
               "sets",
               "-",
               workout["reps"],
               "reps"


            )
    elif choice=="4":
        days= set()
        for workout in day1:
            days.add(workout["day"])
        
        for day in days:
            print(f"\n---{day}---")
            for workout in day1:
                if workout["day"]==day:
                        print(
                        workout["exercise"],
                            "-",
                        workout["sets"],
                            "sets",
                            "-",
                            workout["reps"],
                            "reps"

        )   
    elif choice=="5":
        print("\n---Summary---")
        exe=len(day1)
        print("Total exercise:",exe)
        total_sets=0   
        total_reps=0 
        for workout in day1:
            total_sets +=workout["sets"]
            total_reps +=workout["reps"]
        print("Total sets:",total_sets)
        print("Total reps:",total_reps)

    elif choice=="6":
        break

   
       
   

with open("workout.json","w") as file:
    json.dump(day1, file)