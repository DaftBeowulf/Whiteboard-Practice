"""
# Ring Buffer
When the ring buffer is full and a new element is inserted, 
the oldest element in the ring buffer is overwritten 
with the newest element. 

Implement this behavior in the `RingBuffer` class. 
`RingBuffer` has two methods, `append` and `allValues`. 
The `append` method adds elements to the buffer. 
The `allValues` method returns all of the elements in the buffer 
ordered from oldest to newest. In other words, least-recently 
added elements first, then most-recently added elements. 

buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.allValues()   # should return ['a', 'b', 'c']

buffer.append('d')

buffer.allValues()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.allValues()   # should return ['d', 'e', 'f']
"""


# class RingBuffer:
#     def __init__(self, limit):
#         self.limit = limit
#         self.ring = []

#     def allValues(self):
#         return self.ring

#     def append(self, element):
#         self.ring.append(element)
#         if len(self.ring) > self.limit:
#             del self.ring[0]

# not optimal performance, as append must re-organize entire ring storage when appending past limit

class RingBuffer:
    def __init__(self, limit):
        self.limit = limit
        self.ring = [None]*limit
        self.current = 0

    def allValues(self):
        return self.ring

    def append(self, element):
        self.ring[self.current] = element
        self.current += 1
        if self.current == self.limit:
            self.current = 0

# reassignment of values in ring storage at specified index is constant time, more optimal


buffer = RingBuffer(3)
buffer.append(1)
buffer.append(2)
buffer.append(3)
print(buffer.allValues())
buffer.append(4)
print(buffer.allValues())
