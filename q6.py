import numpy as np
c = np.array([2,3,1])

A = np.array([[1,1,1],
             [-1,-2,1]])

b = np.array([54, -2])

bounds = [(0, None), (0, None), (0, None)]

best_p = -np.inf
best_solution = None

u1_range = np.linspace(0,54,100)
u2_range = np.linspace(0,54,100)
u3_range = np.linspace(0,54,100)

for u1 in u1_range:
    for u2 in u2_range:
        for u3 in u3_range:
            if(u1 + u2 + u3 <= 54) and (-u1 - 2*u2 + u3 <= -2) and (u1>= 0) and (u2>= 0) and (u3>=0):
                p = 2*u1 + 3*u2 + u3
                
                if p > best_p:
                    best_p = p
                    best_solution = (u1,u2,u3)
                    
print("Maximum p: ", best_p)
print("Best solution (u1,u2,u3): ", tuple(map(int,best_solution)))