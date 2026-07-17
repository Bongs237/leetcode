class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        hr1, min1, sec1 = startTime.split(":")
        hr2, min2, sec2 = endTime.split(":")
        
        
        start = int(hr1) * 3600 + int(min1) * 60 + int(sec1)
        end = int(hr2) * 3600 + int(min2) * 60 + int(sec2)
        return end - start