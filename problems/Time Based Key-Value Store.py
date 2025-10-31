class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyStore:
            self.keyStore[key].append([value, timestamp])
        else:
            self.keyStore[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.keyStore[key])
        if n == 0 or self.keyStore[key][0][1] > timestamp:
            return ""

        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2
            if self.keyStore[key][mid][1] > timestamp:
                right = mid
            else:
                left = left + 1
        if self.keyStore[key][left][1] > timestamp:
            left -= 1
        return self.keyStore[key][left][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)