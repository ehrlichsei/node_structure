class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """向队列尾部添加元素"""
        self.items.append(item)

    def dequeue(self):
        """从队列头部移除元素并返回"""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        """返回队列头部的元素但不移除"""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """检查队列是否为空"""
        return len(self.items) == 0

    def size(self):
        """返回队列中元素的个数"""
        return len(self.items)