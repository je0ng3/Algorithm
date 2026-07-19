class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = collections.deque()
        self.k = k
        self.leng = 0

    def enQueue(self, value: int) -> bool:
        if self.leng<self.k:
            self.cq.append(value)
            self.leng += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.leng>0:
            self.cq.popleft()
            self.leng -= 1
            return True
        return False

    def Front(self) -> int:
        return self.cq[0] if self.leng>0 else -1

    def Rear(self) -> int:
        return self.cq[-1] if self.leng>0 else -1

    def isEmpty(self) -> bool:
        return self.leng==0

    def isFull(self) -> bool:
        return self.leng==self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()