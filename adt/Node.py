# 结点类
class Node:
    def __init__(self, value):
        self.value = value
        self.fail = None
        self.tail = 0
        self.child = []
        self.child_value = []
