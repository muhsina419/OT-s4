from scipy.optimize import linprog
# to maximize 20x (chairs) + 30y (tables) [since linprog does minimization by default]
c = [-20, -30]

#coefficients of constraints x + 5y <= 125 && 3x + y <= 80
A = [
    [1, 5], 
    [3, 1]
]

#solutions of constraints
b = [125, 80]

#bounds for x >= 0 and y >=0
x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub = A, b_ub = b, bounds =[x_bounds, y_bounds], method = 'highs')

if result.success:
    chairs = result.x[0]
    tables = result.x[1]
    
    max_profit = -result.fun #converting to positive profit from minimization
    
    print(f"Optimal number of chairs: {chairs}")
    print(f"Optimal number of tables: {tables}")
    print(f"Maximum amount of profit: ${max_profit}")
else:
    print("No solution found.")