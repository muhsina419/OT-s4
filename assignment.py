import numpy as np

def hungarian_algorithm(cost_matrix):
    # Step 1: Subtract the row minima
    cost_matrix = cost_matrix - cost_matrix.min(axis=1)[:, None]

    # Step 2: Subtract the column minima
    cost_matrix = cost_matrix - cost_matrix.min(axis=0)

    # Step 3: Initialize labels for rows and columns
    n = len(cost_matrix)
    u = np.zeros(n)
    v = np.zeros(n)

    # Step 4: Create matching arrays
    ind = np.full(n, -1)

    # Step 5: Start the assignment process
    for i in range(n):
        links = np.full(n, -1)
        mins = np.full(n, np.inf)
        visited = np.zeros(n, dtype=bool)
        marked_i = i
        marked_j = -1
        j = -1
        while True:
            j = -1
            for j_ in range(n):
                if visited[j_]:
                    continue
                cur = cost_matrix[marked_i, j_] - u[marked_i] - v[j_]
                if cur < mins[j_]:
                    mins[j_] = cur
                    links[j_] = marked_j
                if mins[j_] < mins[j] or j == -1:
                    j = j_
            delta = mins[j]
            for j_ in range(n):
                if visited[j_]:
                    u[ind[j_]] += delta
                    v[j_] -= delta
                else:
                    mins[j_] -= delta
            visited[j] = True
            marked_j = j
            marked_i = ind[marked_j]
            if marked_i == -1:
                break
        while True:
            if links[j] != -1:
                ind[j] = ind[links[j]]
                j = links[j]
            else:
                ind[j] = marked_i
                break

    return ind

# Function to compute the total cost of the optimal assignment
def calculate_total_cost(cost_matrix, assignment):
    total_cost = sum(cost_matrix[i, assignment[i]] for i in range(len(assignment)))
    return total_cost

# Example usage:
cost_matrix = np.array([
    [4, 2, 8, 5],
    [2, 3, 7, 6],
    [5, 8, 1, 4],
    [6, 4, 3, 2]
])

# Solve the assignment problem using the Hungarian Algorithm
assignment = hungarian_algorithm(cost_matrix)

# Calculate the total cost of the optimal assignment
total_cost = calculate_total_cost(cost_matrix, assignment)

print(f"Optimal Assignment: {assignment}")
print(f"Total Cost: {total_cost}")