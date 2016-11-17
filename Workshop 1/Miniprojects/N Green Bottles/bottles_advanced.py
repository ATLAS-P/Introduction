"""
In the advanced version of the miniprojects concepts are used that were not covered yet in the workshop connected to the
miniproject.
"""

N = int(input())

def bottleName(n):
    return "bottles" if n > 1 else "bottle"

for i in range(N):
    bottles = N - i

    print(bottles, "green", bottleName(bottles), "hanging on the wall")
    print(bottles, "green", bottleName(bottles), "hanging on the wall")
    print("And if one green bottle should accidentally fall")

    if bottles - 1 == 0:
        print("There'll be no green bottles hanging on the wall")
    else:
        print("There'll be", bottles - 1, "green", bottleName(bottles - 1), "hanging on the wall\n")