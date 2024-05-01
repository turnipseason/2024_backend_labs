class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            print("Size should be a positive integer!")
        self.cap = int(capacity)
        self.cache = {}

    def get(self, key: str) -> str:
        value = self.cache.get(key, '')
        if value:
            del self.cache[key]
            self.cache[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        # если уже есть - обновляем (ставим в конец)
        if key in self.cache:
            del self.cache[key]
        # добавляем новое
        self.cache[key] = value
        # если есть лишнее - убираем
        if len(self.cache) > self.cap:
            print(f"\nCache full. Removed oldest elem: {self.cache.pop(next(iter(self.cache)))}")
            #del self.cache[(next(iter(self.cache)))]


    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
        else:
            print("\nCan't remove a non-existing item")

