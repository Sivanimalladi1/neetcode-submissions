class TimeMap:

    def __init__(self):
        self.value = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.value:
            self.value[key] = []
       
        self.value[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.value.get(key, [])
        start = 0
        end = len(values) - 1
        while start <= end:
            mid = int(start+end)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                start = mid + 1
            else:
                end = mid - 1

        return res
        
