# 문제(스택) 제출답안 2 - 클래스 구현

import sys
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items)!= 0:
            return 0
        return 1

    def push(self,n):
        self.items.append(n)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        return -1

    def top(self):
        if len(self.items) != 0:
            return self.items[-1]
        return -1

    def size(self):
        return len(self.items)


s = Stack()
N = int(sys.stdin.readline())
orders = list(sys.stdin.readline().split() for _ in range(N))
for order in orders:
    if order[0] == 'push':
        s.push(int(order[1]))
    elif order[0] == 'pop':
        print(s.pop())
    elif order[0] == 'size':
        print(s.size())
    elif order[0] == 'empty':
        print(s.isEmpty())
    elif order[0] == 'top':
        print(s.top())
