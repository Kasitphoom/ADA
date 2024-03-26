"""Find optimal interest rate"""

# Optimal Interest Rate Finder
def optimalInterest():
    a = float(input())
    b = float(input())
    c = float(input())

    maxProfit = 0
    maxRate = 0.0
    for rate in range(2001):
        rate = rate / 100
        calc = (a * rate * rate * rate) + (b * rate * rate) + (c * rate)
        if calc > maxProfit:
            maxProfit = calc
            maxRate = rate

    print(maxRate)

optimalInterest()
