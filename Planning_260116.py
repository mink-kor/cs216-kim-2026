# Swimming_pool.py
# January 16, 2026
# Min
# Swimming Pool

# input
Length = int( input("Enter your Length: ") )
Width = int( input("Enter Width: ") )
Depth = int( input("Enter Depth: ") )

# processing
total_volume = Length * Width * Depth
total_gallons = total_volume * (7.5)
number_of_trips = total_volume / (4000)

# output

print( f"total gallons of water = {total_gallons:.2f} total_gallons" )

