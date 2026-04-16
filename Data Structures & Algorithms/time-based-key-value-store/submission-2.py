class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [] 
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res,vals = "", self.timemap.get(key, [])
        
        l,r = 0,len(vals)-1
        while l<=r:
            mid = (l+r)//2
            if vals[mid][-1] <= timestamp:
                res = vals[mid][0]
                l = mid+1
            else:
                r = mid-1

        return res