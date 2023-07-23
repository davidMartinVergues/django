
def solve(meal_cost, tip_percent, tax_percent):
    
    return round(meal_cost*(1+(tip_percent+tax_percent)/100))

print(solve(12.00,20,8))