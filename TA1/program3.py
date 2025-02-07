# Third Program for TA1

#First Pattern (use nested for statement)
#    1
#   12
#  123
# 1234
#12345

#this loop will run 5 times
for i in range(1,6):    
    for j in range(5-i):
        print(" ", end="")
    for k in range(i):
        print(k+1, end="")
    print()
    
#Second Pattern (use nested while statement)

#1
#333
#55555
#666666
#7777777
    
i = 1
# this loop will run 7 times
while i <= 7:   
    j = 1
    while j <= i:
        print(i, end="")
        j = j + 1
    print()
    
    # this code will change the value of i to 3, 5, 7
    if i == 1:
        i = 3
    elif i == 3:
        i = 5
    elif i == 5:
        i = 7
    else:
        break

    