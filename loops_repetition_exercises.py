for letter in "Huntington":
    print( letter, end="-" )
print ()

s = "Huntington  U."

print ( len(s) )
print ()

x = 0
while x < len(s):
    print( x, s[x] )
    x = x + 1
    
print ()

for i in range(0, len(s)):
    print( i, s[i])
print()

#reverse order

s = "work"
x = len(s) - 1

while x >= 0:

    print( x, s[x] )

    x = x - 1
    
s = "Monday"    
for i in range(len(s)-1, -1, -1):
    print( i, s[i] )
print()    
    
    