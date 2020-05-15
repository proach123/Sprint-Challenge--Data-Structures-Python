
import collections

class RingBuffer:
    def __init__(self, capacity = 5, data=[]):
       self.index = 0
       self.capacity = capacity
       self.data = list(data)


    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.index] = item
        else:
            self.data.append(item)
        self.index = (self.index + 1) % self.capacity
        

    def get(self):
        return self.data

