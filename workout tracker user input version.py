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
        sets=int(input("Enter the number of sets:"))
        reps=int(input("Enter your number of reps:"))
        workout ={
             "exercise":exercise,
             "sets":sets,
             "reps":reps
             
        }
 
        day1.append(workout)
        condition = input("Do you wanna add another?").lower()
        while condition!="yes" and condition!="no":
            print("Please Type Yes/No")
            condition = input("Do you wanna add another?").lower()

for exercises in day1:
    print(
        exercises["exercise"],
        "-",
        exercises["sets"],
        "sets",
        "-",
        exercises["reps"],
        "reps"
    )
with open("workout.json","w") as file:
    json.dump(day1, file)