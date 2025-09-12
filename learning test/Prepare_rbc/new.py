class Hashmap:
    def __init__(self,size=10):
        self.size = 10
        self.map = [[] for _ in range(size)]

    def _hash(self,key):
        total = sum(ord(ch) for ch in key)
        return total % self.size

    def put(self,key,value):
        index = self._hash(key)
        bucket = self.map[index]

        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i]=(key,value)

        bucket.append((key,value))
    
    def get(self,key):
        index = self._hash(key)
        bucket = self.map[index]

        for k,v in bucket:
            if k == key:
                print(f"Found key {key} and value {v} at index {index}")
                return v
        
        print(f"{key} is not found")
        return None

    def __repr__(self):
        return str(self.map)
    

h = Hashmap()

h.put("Bob", 85)
h.put("Alice", 90)
h.put("Rob", 70)    # let's assume Bob and Rob collide
h.put("Bob2", 100)

print(h.get("Bob"))
print(h.get("Bob2"))
print(h)