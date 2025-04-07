weights = [1, 2, 3]
values = [6, 10, 12]
capacity = 5

n = len(weights)
dp = [0] * (capacity+1)

for i in range(1,n+1):
    for w in range(capacity, weights[i-1] - 1, -1):
        dp[w] = max(dp[w],values[i-1]+dp[w - weights[i-1]])

print("Answer", dp[capacity])