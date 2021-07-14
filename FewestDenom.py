import math

coins = [int(x) for x in input().split()]
totAmount = int(input())

# Minimum no of coins

# [1,2,4,,5,10]
# 18


for i in range(len(coins) -1 ):
    for j in range(len(coins) - i -1):
        if(coins[j] < coins[j+1]):
            coins[j+1],coins[j] = coins[j],coins[j+1] 

# print(coins)
Remainder = totAmount
coinCount = 0
for coin in coins:
    NearestValue = math.floor(Remainder/coin)
    if(NearestValue != 0):
        Remainder = Remainder%(coin*NearestValue)         
        coinCount = coinCount + NearestValue
    # print(Remainder)
    # input()

print(coinCount)