import math
bitcoinPrices = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
    # declare base lowest possible profit (-inf) to compare other profits against
    high = -math.inf
    for index, price in enumerate(prices):
        for remainder in prices[index:]:
            if remainder-price > high:
                high = remainder-price
    return high


print(find_max_profit(bitcoinPrices))
print(find_max_profit([10, 7, 5, 8, 11, 9]))       # should print 6
print(find_max_profit([1050, 270, 1540, 3800, 2]))  # should print 3530
print(find_max_profit([100, 90, 80, 50, 20, 10]))  # should print -10
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95,
                       43, 11, 47, 67, 89, 42, 49, 79]))   # should print 94
