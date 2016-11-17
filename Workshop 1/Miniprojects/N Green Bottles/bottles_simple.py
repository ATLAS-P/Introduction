N = int(input())

for i in range(N):
    bottles = N - i

    if bottles > 1:
        print(bottles, "green bottles hanging on the wall")
        print(bottles, "green bottles hanging on the wall")
    else:
        print(bottles, "green bottle hanging on the wall")
        print(bottles, "green bottle hanging on the wall")

    print("And if one green bottle should accidentally fall")
    
    if bottles - 1 == 0:
        print("There'll be no green bottles hanging on the wall")
    elif bottles - 1 == 1:
        print("There'll be 1 green bottle hanging on the wall\n")
    else:
        print("There'll be", bottles - 1, "green bottles hanging on the wall\n")