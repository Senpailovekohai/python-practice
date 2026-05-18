day1=[
    {"exercise":"Bench Press","sets":3,"reps":4},
    {"exercise":"Incline Bench Press","sets":3,"reps":4},
    {"exercise":"Cable fly","sets":3,"reps":4},
    {"exercise":"ropepull down ","sets":3,"reps":4},
    {"exercise":"Overhead tricep pull ","sets":3,"reps":4},
]
print("Day 1: Chest and Triep Split")
for workout in day1:
    print(
        workout["exercise"],
        "-",
        workout["sets"],
        "sets-",
        workout["reps"],
        "reps-"
    )
day2=[
    
    {"exercise":"pull up","sets":3,"reps":4},
    {"exercise":"Romanain Deadlift","sets":3,"reps":4},
    {"exercise":"Face-Pull","sets":3,"reps":4},
    {"exercise":"Bicep Crul","sets":3,"reps":4},
    {"exercise":"Preacher Crul","sets":3,"reps":4},
    {"exercise":"Hammer Crul","sets":3,"reps":4}

]
print("Day-2: Back and Bicep Spilt")
for workout in day2:
    print(
        workout["exercise"],
        "-",
        workout["sets"],
        "sets-",
        workout["reps"],
        "reps"
    )
print("Day 3: Rest Day")
day4=[
    {"exercise":"leg Press","sets":3,"reps":4},
    {"exercise":"Squate","sets":3,"reps":4},
    {"exercise":"Calf Raise","sets":3,"reps":4},
    {"exercise":"Cardio","sets":3,"reps":4},
  
    
]
print("Day 4: Leg and Cardio Split")
for workout in day4:
    print(
        workout["exercise"],
        "-",
        workout["sets"],
        "sets-",
        workout["reps"],
        "reps-"
    )

day5=[
    {"exercise":"Shoulder Press","sets":3,"reps":4},
    {"exercise":"Laternal Raise","sets":3,"reps":4},
    {"exercise":"Rear Delt fly","sets":3,"reps":4},
    {"exercise":"leg Raise","sets":3,"reps":4},
    {"exercise":"Crunchs","sets":3,"reps":4}
    
]
print("Day 5: Shoulder and Abs Split")
for workout in day5:
    print(
        workout["exercise"],
        "-",
        workout["sets"],
        "sets-",
        workout["reps"],
        "reps-"
    )
print("Rest Day and Repeat Again")