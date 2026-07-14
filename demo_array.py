class array:
    def __init__(self, capacity =4 ):
        self.capacity = capacity
        self.length = 0
        self.array = [] * capacity
        
        
    def __len__(self):
        return self.length
    
    def get(self,index):
        if index >= self.capacity or index < 0:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def set(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("out of bounds")
        self.array[index] = value
        
    

    def append(self, value):
        pass

    def _resize(self, new_capacity):
        pass

    def delete(self, index):
        pass

    def __repr__(self):
        pass


if __name__ == "__main__":
    arr = DynamicArray()
    # test your methods here