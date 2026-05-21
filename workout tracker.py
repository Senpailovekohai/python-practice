def show_workout(day_name , workout_list):
    print(day_name)
    for workout in workout_list:
        print(workout["exercise"],
          "-",
          workout["sets"],
          "-sets",
          workout["reps"],
          "-reps"

    )


day1=[
    {"exercise":"Bench Press","sets":3,"reps":4},
    {"exercise":"Incline Bench Press","sets":3,"reps":4},
    {"exercise":"Cable fly","sets":3,"reps":4},
    {"exercise":"ropepull down ","sets":3,"reps":4},
    {"exercise":"Overhead tricep pull ","sets":3,"reps":4},
]

day2=[
    
    {"exercise":"pull up","sets":3,"reps":4},
    {"exercise":"Romanain Deadlift","sets":3,"reps":4},
    {"exercise":"Face-Pull","sets":3,"reps":4},
    {"exercise":"Bicep Crul","sets":3,"reps":4},
    {"exercise":"Preacher Crul","sets":3,"reps":4},
    {"exercise":"Hammer Crul","sets":3,"reps":4}

]


day4=[
    {"exercise":"leg Press","sets":3,"reps":4},
    {"exercise":"Squate","sets":3,"reps":4},
    {"exercise":"Calf Raise","sets":3,"reps":4},
    {"exercise":"Cardio","sets":3,"reps":4},
  
    
]


day5=[
    {"exercise":"Shoulder Press","sets":3,"reps":4},
    {"exercise":"Laternal Raise","sets":3,"reps":4},
    {"exercise":"Rear Delt fly","sets":3,"reps":4},
    {"exercise":"leg Raise","sets":3,"reps":4},
    {"exercise":"Crunchs","sets":3,"reps":4}
    
]

show_workout("Day 1: Cheast and Tricep",day1)
show_workout("Day2:Back and bicep split",day2)
print("Day 3: Rest Day")
show_workout("Day 4: Rest and Recovery Day",day4)
show_workout("Day 5: Shoulder and Abs",day5)
print("Rest Day and Repeat Again")