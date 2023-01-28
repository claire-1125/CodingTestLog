""""<논리흐름>
500원, 100원, 50원, 10원짜리 동전 무한 개
거스름돈 N원
거슬러줘야 할 최소한의 동전 개수?"""

"""1260
500 2...260
100 2...60
50 1...10
10 1...0"""

"""나눈 것의 몫만큼 count
나눈 것의 나머지로 다시 몫 구하기"""

# 동전 리스트에서 큰 단위부터 작성함에 유의!
# 서로가 서로의 약수/배수 관계이므로 이러한 방식 가능

def solution(money):
    cnt = 0
    for elem in [500, 100, 50, 10]:
        cnt += money // elem
        money %= elem
    return cnt

print(solution(int(input())))

# 또 다른 풀이
# n = int(input())
# 
# a, a_ = n // 500, n % 500
# b, b_ = a_ // 100, a_ % 100
# c, c_ = b_ // 50, b_ % 50
# d, d_ = c_ // 10, c_ % 10
#
# # 최소 동전 개수
# print(a+b+c+d)