def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a DP table with (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    
    # Build the table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w],
                               dp[i-1][w - weights[i-1]] + values[i-1])
        print(dp)
    # print(dp)
    return dp[n][capacity]

# Example usage:
weights = [1, 2, 3]
values = [6, 10, 12]
capacity = 5
max_value = knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
