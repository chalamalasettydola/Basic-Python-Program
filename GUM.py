#wr to check the grade using marks#
marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("The grade is A \nVery good")
elif marks >= 70 and marks < 90:
    print("The grade is B \nGood")
elif marks >= 40 and marks < 70:
    print("The grade is C \nImprove")
else:
    print("You have failed \nRequired more improvement")

