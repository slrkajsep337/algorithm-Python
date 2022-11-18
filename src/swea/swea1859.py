


T = int(input())

for i in range(T):
    n = int(input())
    prices = list(map(int, input().split()))

    mprice = prices[-1]
    rst = 0

    for j in range(n-2, -1, -1):
        if prices[j] >= mprice:
            mprice = prices[j]
        else:
            rst += mprice-prices[j]
    print("#{} {}".format(i+1, rst))






