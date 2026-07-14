class Array:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.length = 0
        self.array = [None] * capacity

    def __len__(self):
        return self.length

    def get(self, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def set(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("out of bounds")
        self.array[index] = value

    def append(self, value):
        if self.length >= self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.length] = value
        self.length += 1

    def _resize(self, new_capacity):
        additional_slots = new_capacity - self.capacity
        for _ in range(additional_slots):
            self.array.append(None)
        self.capacity = new_capacity

    def delete(self, index):
        if index >= self.length or index < 0:
            raise IndexError("out of bounds")
        if index == self.length -1 :
            self.array[index] = None
        else:
            for x in range(index, self.length):
                if x+1 < self.length:
                    self.set(x, self.get(x+1))
        self.set(self.length-1, None)
        self.length -= 1
        # shifting logic still needs to be added here — this was
        # the part you hadn't finished yet
        

    def __repr__(self):
        return f"Array({self.array[:self.length]})"