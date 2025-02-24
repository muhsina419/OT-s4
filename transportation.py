import numpy as np

# Function to calculate penalties for each row and column
def calculate_penalties(costs, supply, demand):
    row_penalties = []
    column_penalties = []

    # Row penalties
    for i in range(len(costs)):
        if supply[i] > 0:  # Consider only rows with remaining supply
            sorted_costs = sorted([costs[i][j] for j in range(len(costs[i])) if demand[j] > 0])
            row_penalties.append(sorted_costs[1] - sorted_costs[0] if len(sorted_costs) > 1 else 0)
        else:
            row_penalties.append(-1)  # Mark exhausted rows

    # Column penalties
    for j in range(len(costs[0])):
        if demand[j] > 0:  # Consider only columns with remaining demand
            col_costs = [costs[i][j] for i in range(len(costs)) if supply[i] > 0]
            sorted_costs = sorted(col_costs)
            column_penalties.append(sorted_costs[1] - sorted_costs[0] if len(sorted_costs) > 1 else 0)
        else:
            column_penalties.append(-1)  # Mark exhausted columns

    return row_penalties, column_penalties

# Function to find the initial feasible solution using VAM
def VAM(supply, demand, costs):
    supply = supply.copy()  # Copy to avoid modifying original lists
    demand = demand.copy()
    rows, cols = len(costs), len(costs[0])
    transportation_plan = np.zeros((rows, cols))

    # Loop until all supply and demand are met
    while np.sum(supply) > 0 and np.sum(demand) > 0:
        row_penalties, column_penalties = calculate_penalties(costs, supply, demand)

        # Find the maximum penalty
        max_row_penalty = max(row_penalties)
        max_col_penalty = max(column_penalties)

        # Choose the row or column with the highest penalty
        if max_row_penalty >= max_col_penalty:
            # Select the row with maximum row penalty
            row_index = row_penalties.index(max_row_penalty)

            # Find the column with the minimum cost in the selected row (considering only available columns)
            min_col_index = np.argmin([costs[row_index][j] if demand[j] > 0 else float('inf') for j in range(cols)])

            # Allocate the maximum possible quantity to the selected cell
            allocation = min(supply[row_index], demand[min_col_index])
            transportation_plan[row_index][min_col_index] = allocation
            supply[row_index] -= allocation
            demand[min_col_index] -= allocation
        else:
            # Select column with maximum penalty
            col_index = column_penalties.index(max_col_penalty)

            # Find the row with the minimum cost in the selected column (considering only available rows)
            min_row_index = np.argmin([costs[i][col_index] if supply[i] > 0 else float('inf') for i in range(rows)])

            # Allocate the max possible quantity to the selected cell
            allocation = min(supply[min_row_index], demand[col_index])
            transportation_plan[min_row_index][col_index] = allocation
            supply[min_row_index] -= allocation
            demand[col_index] -= allocation

    return transportation_plan

# Function to calculate the total cost of the transportation plan
def calculate_total_cost(transportation_plan, costs):
    total_cost = np.sum(transportation_plan * np.array(costs))
    return total_cost

# Example Input
supply = [30, 70, 50]  # Supply at each source
demand = [40, 60, 50]  # Demand at each destination
costs = [
    [8, 6, 10],  # Costs from source 1 to destinations 1, 2, 3
    [9, 5, 7],   # Costs from source 2 to destinations 1, 2, 3
    [3, 2, 4]    # Costs from source 3 to destinations 1, 2, 3
]

# Get the transportation plan using VAM
transportation_plan = VAM(supply, demand, costs)

# Calculate the total cost
total_cost = calculate_total_cost(transportation_plan, costs)

# Output Results
print("Transportation Plan:")
print(transportation_plan)
print(f"Total Transportation Cost: {total_cost}")
