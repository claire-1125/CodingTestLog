"""
1 = 2*0+1
3 = 2*1+1
5 = 2*2+1
7 = 2*3+1
9 = 2*4=1
"""
n = int(input())

for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))