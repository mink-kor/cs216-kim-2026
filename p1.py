# p1.py
# January 19, 2026
# Min Kim
# Planning IPO

# Input

print("Enter number of steps")
steps = int(input())
print("Enter stride distance in inches")
stride_inches = int(input())


# Processing
inches_walked = steps * stride_inches

# 1 mile = 63,360

miles = inches_walked / 63360



# Output

print(f"You walked {steps:,} steps which is {miles:.2f} miles")

difference = steps - 10000

if steps < 10000:
    print (f"You need {abs(difference):,} more steps to reach 10,000")

elif steps > 10000:
    print (f"You were {difference:,} steps over 10,000")
else:
    print ( "You walked exactly 10,000 steps")
