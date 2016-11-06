#Every time the code is run, the for loop sets one variable.
for i in range(5):
    print(i)

print("Done!")

'''
The output of the above code is:

0
1
2
3
4
Done!

For now, we're only using for loops in combination with range(). This gives the following options:
'''

for i in range(7):
    # loops i from 0 (included) to 7 (excluded):
    # 0, 1, 2, 3, 4, 5, 6

for i in range(5, 9):
    # loops i from 5 (included) to 9 (excluded):
    # 5, 6, 7, 8

for i in range(10, 2, -2):
    # loops i from 10 (included) to 2 (excluded) with steps of -2:
    # 10, 8, 6, 4

#Note. The loop stops before it reaches the end number.