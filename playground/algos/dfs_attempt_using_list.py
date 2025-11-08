def dfs(depth,digits,prefix,nodes):
    if depth==0:
        nodes.append(prefix)
        return nodes
    for digit in digits:
        dfs(depth-1,digits,prefix+digit,nodes)
    return nodes
    

print(dfs(7, ['0','1','2','3'],'',[]))