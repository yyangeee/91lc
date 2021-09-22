from random import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        self.arr = []
        self.n = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        self.data[val] = self.n
        self.arr.append(val)
        self.n += 1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data:
            return False
        i = self.data[val]
        # 更新data
        self.data[self.arr[-1]] = i#和最后一项交换
        self.data.pop(val)#因为没有重复的val,so just pop val
        # 更新arr
        self.arr[i] = self.arr[-1]
        # 删除最后一项
        self.arr.pop()
        self.n -= 1

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return self.arr[int(random() * self.n)]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
