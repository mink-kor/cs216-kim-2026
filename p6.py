# p6.py
# spring 2026
# Min Kim
# 3/13/2026
# The purpose of this assignment is to gain an understanding of how to 
# create and use lists

from random import *

# *** lists ***

#1 Create a list to hold 15 items, all set to zero
print("List 1")
print()
num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print( f"Number of items in num = {len(num)}")
print(num)
print()

i = 0 
while i < len(num):
    print( num[i], end=" ")
    i = i + 1
print()


#2 Use a for loop to set all items in the list equal to 2026
print()
print("List 2")
print()

for i in range (len(num)):
    num[i] = 2026
   
print(num[i]) 
print()



#3 Using a for loop, add 100 to all items in the list
print ("List 3")
print()

for i in range (len(num)):
    num[i] = num [i] + 100
    
print(num [i])
print()

#4 Using a for loop, set all items in the list to a random number
# in the range 2026 <= n <= 2099

print ("List 4")
print()

for i in range (len(num)):
    num [i] = randint(2026, 2099)

print(num)
print()

#5 Display the smallest and largest values from the list

print ("List 5")
print()

small= min(num)
big = max(num)

print("min:", small)
print("max:", big)
print()



#6 Create a function called avg that returns the average value of
# all items in the list.

print("List 6")
print ()

def avg(temp):
    return sum(temp) / len(temp)

print("avg:", avg(num))
print()

#7 Sort your list

print("List 7")
print ()
print("after sorting")


# ascending order
num.sort()
print(num)
print()

# descending order
num.reverse()
print(num)
print()


#8 Create a function called countRange that takes a list and a min and max
# range and returns a count of the number of list items that are in the
# range count = number of items between m and n inclusive ie. m <= item <= n

print ("List 8")
print()

def countRange(temp, m, n):
    count = 0
    for item in temp:
        if item >= m and item <= n:
            count = count + 1
    return count

print("2020-2030:", countRange( num, 2020, 2030 ))
print("2050-2055:", countRange( num, 2050, 2055 ))
print()

#9 Create a function called getRandom that returns a random number
#  from your list.  Call the function x5 times.

print ("List 9")
print()

def getRandom(temp):
    return choice(temp)

for i in range (5):
    print(getRandom(num))

print()

# Given
verse = "Trust in the Lord with all your heart and lean not on your own understanding"
citation = "Proverbs 3:5"
words = []

#10 Use the split() method to store the words from the verse in a list called words

print ( "List 10")
print()

words = verse.split()
print( words )
print()

#11 Use slice ie. [x:y] to display the first four words in the list (should work with any list)

print( "List 11")
print()

print( words[0:4] )
print()

#12 Use slice ie. [x:y] to display the last three words (should work for any list)

print( "List 12")
print()

print( words[-3:])
print()


#13 Add the citation to the end of the words list using append
print( "List 13")
print()

words.append( citation )
print( words )
print()

#14 Remove the citation from the end of the word list
print( "List 14")
print()

words.pop( )
print( words )
print()

#15 Use a while loop to display all of the words in the list
print( "List 15")
print()

i = 0
while i < len(words):
    print(words[i])
    i = i +1 
    #end while loop
print()

#16 Use a for loop with an index ie. words[i] to display all words in the list
print( "List 16")
print()

i = 0 

for i in range (len(words)):
    print(words[i])
    print()

#17 Use the IN operator to display all of the words
print( "List 17")
print()

for word in words:
    print(word)
    print()

#18 display all of the words in reverse order

print( "List 18")
print()

for word in reversed(words):
    print(word)
print() 

#19 Remove the word "own" from the word list
print( "List 19")
print()

words.pop(13)
print( words )
print()

#20 Replace the word "lean" with "rely" in the word list
print( "List 20")
print()

words[9] = "rely"
print( words )
print()

#21 Use the join operator to take each word and recreate the verse, storing as a string in variable verse_v2
print( "List 21")
print()

verse_v2 = " ".join(words)
print( verse_v2 )
print()



# -- end --


#*** end of code ****