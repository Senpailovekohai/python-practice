day1=[]
condition="yes"
while condition == "yes":
  
    exercise=input("Enter the exercise:")
    sets=int(input("Enter the number of sets:"))
    reps=int(input("Enter the number of reps:"))
    workout={
    "exercise":exercise,
    "sets":sets,
    "reps":reps
    }
    day1.append(workout)
    condition=input("Do you still want to add another exercise?").lower()
    

        
for show in day1:
        print(
           show["exercise"],
       "-",
       show["sets"],
       "sets",
       show["reps"],
       "reps"
    
  
        )
print("That's it!!")
        
        


