class MyLinkedList:

    def __init__(self):
        self.q = []
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.q[index]

    def addAtHead(self, val: int) -> None:
        self.q.insert(0, val)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.q.append(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.q.insert(0, val)
            self.size += 1
        elif index <= self.size:
            self.q.insert(index, val)
            self.size += 1
        # else: do nothing

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            self.q.pop(index)
            self.size -= 1