# Zhang, Jake Jiekai
# G10A
"""
Sample output(letter J):
@@@@@@@
   @
   @
   @
@  @
 @@
"""

# 6 rows
for row in range(6):
    # First row
    if row == 0:
        print("@@@@@@@")
    # Second to the last row
    elif row == 4:
        print("@  @")
    # Last row
    elif row == 5:
        print(" @@")
    # Other rows
    else:
        print("   @")
