from scipy.optimize import linprog
c = [-200, -150]


A = [
    [1, 1],
    [20,10],
    [10,15]
]

#solutions of constraints
b = [60,1200, 600]

#bounds for x >= 0 and y >=0
x_bounds = (20, None)
y_bounds = (10, None)

result = linprog(c, A_ub = A, b_ub = b, bounds =[x_bounds, y_bounds], method = 'highs')

if result.success:
    wheat = result.x[0]
    barley = result.x[1]
    
    max_profit = -result.fun #converting to positive profit from minimization
    
    print(f"Optimal number of wheat: {wheat}")
    print(f"Optimal number of barley: {barley}")
    print(f"Maximum amount of profit: ${max_profit}")
else:
    print("No solution found.")