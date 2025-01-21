# Function to solve 0/1 Knapsack problem using dynamic programming
def knapsack_01(values, weights, capacity):
    n = len(values)  # Number of items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]  # DP table

    # Fill the DP table
    for i in range(1, n + 1):  # Iterate through items
        for w in range(1, capacity + 1):  # Iterate through possible weights
            if weights[i - 1] <= w:
                # Either include the current item or exclude it
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # If the item cannot be included (it exceeds the capacity)
                dp[i][w] = dp[i - 1][w]

    # dp[n][capacity] contains the maximum value that can be achieved with capacity W
    return dp[n][capacity]

# Function to input the knapsack problem
def input_knapsack():
    n = int(input("Enter the number of items: "))
    values = list(map(int, input("Enter the values of the items (separated by spaces): ").split()))
    weights = list(map(int, input("Enter the weights of the items (separated by spaces): ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    return values, weights, capacity

# Main program
values, weights, capacity = input_knapsack()  # Get user input
max_value = knapsack_01(values, weights, capacity)  # Compute the maximum value
print(f"Maximum value in the knapsack: {max_value}")
