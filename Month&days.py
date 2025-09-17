month = int(input("Enter the month (1-12): "))

if month == 2:
    print("28 or 29 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
else:
    print("It is an invalid month")

