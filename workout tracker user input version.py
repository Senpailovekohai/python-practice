import json
import os
if os.path.exists("workout.json"):
    with open("workout.json","r") as file:
        day1 = json.load(file)
else:
    day1=[]

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
        day=input("Enter which day is it for?")
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
delete=input("Do you want to delete any workout?").lower()
if delete=="yes":
    user_input=input("Which exercise you wanna delete?")
    for workout in day1:
        if workout["exercise"]==user_input:
            day1.remove(workout)
            print("Sucessfully Deleted!!")
            break
    else:
            print("Exercise not found.")
            
while delete!="yes" and delete!="no":
    print("Please enter Yes/No")
    delete=input("Do you want to delete any workout?").lower()
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

with open("workout.json","w") as file:
    json.dump(day1, file)