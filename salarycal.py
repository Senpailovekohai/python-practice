rate=float(input("Enter your basic rate:"))
hour=float(input("Enter your number of working hours:"))
years=float(input("Enter your numbers of year in work:"))
pay=rate*hour
print("Your basic salary without any condition:",pay)
if hour>200:
    pay=pay+(hour-200)*rate*1.5
    print("Your monthly salary with bonus of over 200 hours is:",pay)


if years>4.5:
    pay=pay+10000
    print("Your salary with experience beneift  ",pay)

if pay>300000:
    pay=pay-0.10*pay
else:
    pay=pay-0.033*pay

print("Your final monthly salary after tax deduction is:",pay)



