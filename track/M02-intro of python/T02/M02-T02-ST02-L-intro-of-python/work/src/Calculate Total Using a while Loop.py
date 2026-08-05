# Read the value of n
n=int(input())

# Initialize the counter and total
count=1
total=0
# Calculate the total using a while loop
while n>=count:
    total=count+total
    count=count+1

# Display the total
print (f"Total: {total}")