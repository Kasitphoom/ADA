def max_profit(rental_fee, sales):
    n = len(sales)
    max_profit = 0
    
    for start in range(n):
        total_income = 0
        total_cost = 0
        
        for end in range(start, n):
            total_income += sales[end]
            total_cost += rental_fee
            
            if total_income - total_cost > max_profit:
                max_profit = total_income - total_cost
                
    return max_profit if max_profit > 0 else "No"


rental_fee = int(input())
sales = list(map(int, input().split()))
print(max_profit(rental_fee, sales)) 
