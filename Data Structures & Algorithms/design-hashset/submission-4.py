class MyHashSet:

    def __init__(self):
        self.hash_set = {}
        

    def add(self, key: int) -> None:
        if self.hash_set.get(key, 0) == 0:
            self.hash_set[key] = self.hash_set.get(key, 0) + 1

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set[key] -=1

    def contains(self, key: int) -> bool:
        print(self.hash_set)
        return bool((key in self.hash_set) and self.hash_set[key]==1)

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)