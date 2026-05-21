import json
day1=[
    {"exercise":"Bicep Curls","sets":3,"reps":4}
]
with open("workout.json","w") as file:
    json.dump(day1,file)