# ===================================================================
#   PYTHON PROGRAMMING (Laboratory Activity 4B: Set and Dictionary)
#               Submitted by: JULIUS FRANCIS DE LEON
#                      Date: March 04, 2025
# ===================================================================

# These are the sets of elements in PROBLEM 1
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# How many elements are there in set A and B?
print(f"Number of elements in A and B: {len(A & B)}")

# How many elements are there in B that are not part of A and C?
print(f"Number of elements in B that are not part of A and C: {len(B - (A | C))}")

# Show the following using set operations
# [h, i, j, k]
print(f" 1. {sorted(C - A)}")

# [c, d, f]
print(f" 2. {sorted(A & C)}")

# [b, c, h]
print(f" 3. {sorted(B & (A | C))}")  

# [d, f]
print(f" 4. {sorted((A & C) - B)}")  

# [c]
print(f" 5. {sorted(A & B & C)}")

# [l, m, o]
print(f" 6. {sorted(B - (A | C))}")

input("Press ENTER to continue...")
