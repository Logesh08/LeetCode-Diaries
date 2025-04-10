def dfs(depth, items, prefix='', results=None):
    if results is None:
        results = []
    if depth == 0:
        results.append(prefix)
        return results
    for digit in items:
        dfs(depth - 1, items, prefix + digit, results)
    return results

print(dfs(3, ['0','1','2','3']))