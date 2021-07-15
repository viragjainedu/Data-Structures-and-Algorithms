# Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. 
# Determine the maximum value obtainable by cutting up the rod and selling the pieces.

5
[2,3,2,3,5]

def Solve(prices,rodLength):
    
    # if(rodLength == 1):
    #     return prices[0]

    MaxValue = [0]*(rodLength+1)

    for i in range(1,rodLength+1):
        for j in range(1,i+1):
            MaxValue[i] = max(MaxValue[i], prices[j - 1] + MaxValue[i - j])


    return MaxValue[rodLength]

if __name__ == '__main__':
    prices = [1, 3, 2, 3, 5, 17, 17, 20]
    rodLength = 5        # rod length
    print(Solve(prices,rodLength))