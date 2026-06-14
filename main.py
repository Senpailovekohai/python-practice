expense = [{"name": "latte", "amount": 500}]

exp = "rr"
for cost in expense:
    if cost["name"] == exp:
        print("found")
        break
else:
    print("not found")