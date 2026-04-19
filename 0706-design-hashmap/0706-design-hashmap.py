class MyHashMap:

    def __init__(self):
        self.size = 10007
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        existed = False 
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                existed = True
                break
        if not existed:      
            self.table[idx].append((key, value))        

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)         
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                break

    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)