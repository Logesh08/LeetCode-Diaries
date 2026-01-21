class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        normalizeHour = (5 * hour) + (5 * (minutes / 60))
        segments = abs(minutes - normalizeHour)
        angle =  6 * segments
        return min(angle, 360 - angle)