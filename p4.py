# ** Bowling Scores **
# ** Min Kim **
# **January 19, 2026 **
# sentinel-controlled loop to determine high, low, average
# bowling scores

min = 301
max = -1
numberBowlers = 0
totalScore = 0

# Processing using Sentinel loop

# ** add your code here **
# Input
score = int(input("Enter score 1 (-1 to quit): "))

scoreNum = 1

#example of invalid entry
while score !=-1:
    if score < 0 or score > 300:
        print("Error: Invalid score, Expecting 0-300")
        score = int(input(f"Enter score {scoreNum} (-1 to quit): "))
    else:
        numberBowlers += 1
        totalScore += score
        if score > max:
            max = score
        if score < min:
            min = score
        scoreNum += 1
        score = int(input(f"Enter score {scoreNum} (-1 to quit): "))
        
    
# Output
if numberBowlers > 0:
    avg = totalScore / numberBowlers
    print()
    print(f"Number of Bowlers: {numberBowlers}")
    print(f"High Score: {max}")
    print(f"Low Score: {min}")
    print(f"Avg Score: {avg:.2f}")
else:
    print()
    print("No scores were entered.")