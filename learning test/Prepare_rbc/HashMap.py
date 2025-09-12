class hashmap:
    def __init__(self,size=10):
        self.size = size
        self.map = [[] for _ in range(size)]
    
    def _hash(self,key):
        total = sum(ord(ch) for ch in key)
        return total % self.size
    
    def put(self,key,value):
        index = self._hash(key)
        bucket = self.map[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print(f"Updated key '{key}' at index {index}: {bucket}")
                return
        
        bucket.append((key, value))
        print(f"Inserted key '{key}' at {index}: {bucket}")
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.map[index]

        for k,v in bucket:
            if k == key:
                print(f"Found key {key} at {index}: {v}")
                return v
        print(f"Key {key} not found")
        return None
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.map[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        

    

h = hashmap()

h.put("Bob", 85)
h.put("Alice", 90)
h.put("Rob", 70)    # let's assume Bob and Rob collide
h.put("Bob2", 100)

print(h.get("Bob"))
print(h.get("Bob2"))
