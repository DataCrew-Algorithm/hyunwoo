# 시간초과

import sys

input = sys.stdin.readline

def fibonacci(n):
    global count_zero, count_one
    if n == 0:
        count_zero += 1
        return count_zero
    elif n == 1:
        count_one += 1
        return count_one
    else:
        return fibonacci(n-1) + fibonacci(n-2)



N = int(input())

for i in range(N):
    count_zero = 0
    count_one = 0
    a = int(input())
    fibonacci(a)
    print(count_zero, count_one)

# ===================================================================
# N이 최대가 40이라 꼼수를 좀 써봄
# 68ms

import sys

input = sys.stdin.readline

zero = [0 for i in range(41)]
one = [0 for i in range(41)]

zero[0] = 1
one[1] = 1

for i in range(2, 41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

N = int(input())

for i in range(N):
    n = int(input())
    print(zero[n], one[n])