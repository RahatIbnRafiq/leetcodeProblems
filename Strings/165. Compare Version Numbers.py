class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = version1.split(".")
        version2 = version2.split(".")
        version1 = [int(x) for x in version1]
        version2 = [int(x) for x in version2]
        for i in range(0,max(len(version1),len(version2))):
            v1 = version1[i] if i < len(version1) else 0
            v2 = version2[i] if i < len(version2) else 0
            if v1 > v2: return 1
            elif v1 < v2: return -1
        return 0
