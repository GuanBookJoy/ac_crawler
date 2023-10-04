# AC自动机类
from adt.Node import Node


class Automaton:
    def __init__(self):
        self.root = Node("r")
        self.count = 0

    # 加入模式串，建立tire树
    def add_pattern(self, pattern):
        self.count += 1
        p = self.root
        for character in pattern:
            if character not in p.child_value:
                child = Node(character)
                p.child.append(child)
                p.child_value.append(character)
                p = child
            else:
                p = p.child[p.child_value.index(character)]
        p.tail = self.count

    # 计算Fail指针
    def cal_fail(self):
        queue_list = [self.root]
        while len(queue_list):
            temp = queue_list[0]
            queue_list.remove(temp)
            for node in temp.child:
                if temp == self.root:
                    node.fail = self.root
                else:
                    p = temp.fail
                    while p:
                        if node.value in p.child_value:
                            node.fail = p.child[p.child_value.index(node.value)]
                            break
                        p = p.fail
                    if not p:
                        node.fail = self.root
                queue_list.append(node)

    # 模式匹配
    def run_ac(self, mode):
        p = self.root
        cnt = {}
        for sub_str in mode:
            while sub_str not in p.child_value and p is not self.root:
                p = p.fail
            if sub_str in p.child_value:
                p = p.child[p.child_value.index(sub_str)]
            else:
                p = self.root
            temp = p
            while temp is not self.root:
                if temp.tail:
                    if temp.tail not in cnt:
                        cnt.setdefault(temp.tail)
                        cnt[temp.tail] = 1
                    else:
                        cnt[temp.tail] += 1
                temp = temp.fail
        return cnt
