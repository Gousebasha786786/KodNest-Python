# Read marks, attendance and project completion status
marks=int(input())
attendance=int (input())
project=input()
# Check the academic requirements
if marks >=60 and attendance >=75:
    if project == "yes":
        # Check the project completion status
        print ("Eligible")
    else:
        print ("Not Eligible")
else:
    print ("Not Eligible")