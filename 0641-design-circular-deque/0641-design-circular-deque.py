class MyCircularDeque:

    def __init__(self, k: int):
        self.cd = collections.deque()
        self.k = k
        self.leng = 0

    def insertFront(self, value: int) -> bool:
        if self.leng<self.k:
            self.cd.appendleft(value)
            self.leng+=1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.leng<self.k:
            self.cd.append(value)
            self.leng+=1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.leng>0:
            self.cd.popleft()
            self.leng-=1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.leng>0:
            self.cd.pop()
            self.leng-=1
            return True
        return False

    def getFront(self) -> int:
        if self.leng>0:
            return self.cd[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.leng>0:
            return self.cd[-1]
        return -1

    def isEmpty(self) -> bool:
        return self.leng==0

    def isFull(self) -> bool:
        return self.leng==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()