def show_workout( days , exercise):
    print(days)
    for workout in exercise:
        print(
            workout["exercise"],
            "-",
            workout["sets"],
            "-sets",
            workout["reps"],
            "-reps"
        )
day1=[
          {"exercise":"Bench Press","reps":3,"sets":4},
          {"exercise":"Bicep curls","reps":3,"sets":4}
        ]

day2=[
            {"exercise":"leg press","reps":3,"sets":4},
            {"exercise":"abs","reps":3,"sets":4}

        ]
show_workout("Chest day",day1)
show_workout("leg day",day2)