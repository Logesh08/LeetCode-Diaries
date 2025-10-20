# Final Value of Variable After Performing Operations

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            eval(operation)
        return X