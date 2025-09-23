class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        ind = 0
        while ind < len(version1) and ind < len(version2):
            a = int(version1[ind])
            b = int(version2[ind])
            if a > b:
                return 1
            elif b > a:
                return -1
            ind += 1
        while ind < len(version1):
            if int(version1[ind]) != 0:
                return 1
            ind += 1
            
        while ind < len(version2):
            if int(version2[ind]) != 0:
                return -1
            ind += 1
            
        
        return 0