def knapsack_optimized(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse backwards to avoid using the same item more than once
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        print(dp)
    return dp[capacity]

# Example usage:
weights = [1, 2, 3]
values = [6, 10, 12]
capacity = 5
max_value_optimized = knapsack_optimized(weights, values, capacity)
print("Maximum value in knapsack (optimized):", max_value_optimized)
