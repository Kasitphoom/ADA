"""Booth rental"""

"""Function finding maximum profit"""
def booth_rental():
    rent_rate = int(input())
    input_array = list(map(int, input().split()))
    max_profit = 0
    total = 0
    for number in input_array:
        total += number - rent_rate
        if total <= 0:
            total = 0
        else:
            if total > max_profit:
                max_profit = total

    print("No" if max_profit == 0 else max_profit)

booth_rental()
