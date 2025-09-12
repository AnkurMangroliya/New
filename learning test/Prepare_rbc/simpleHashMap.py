class SimpleHashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [None] * size
    
    def _hash(self,key):
        total = sum(ord(ch) for ch in key)
        return total % self.size
    
    def put(self,key,value):
        index = self._hash(key)
        self.map[index] = value
    
    def get(self,key):
        index = self._hash(key)
        return self.map[index]

s = SimpleHashMap()
s.put("Bob", 85)     # Bob goes to index 5
s.put("Alice", 90)
print(s.get("Bob"))