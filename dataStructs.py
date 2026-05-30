class Stack:
    def __init__(self, stack: list | set | tuple):
        self.stack = list(stack)

    def pop(self):
        if not self.stack:
            raise ValueError('Stack is empty, cannot pop.')
        return self.stack.pop()

    def push(self, pushed):
        self.stack.append(pushed)

    def __repr__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return Stack(self.stack[key])
        return self.stack[key]


class Queue:
    def __init__(self, queue: list | set | tuple):
        self.queue = list(queue)

    def dequeue(self):
        if not self.queue:
            raise ValueError('Queue is empty, cannot dequeue.')
        return self.queue.pop(0)

    def enqueue(self, enqueued):
        self.queue.append(enqueued)

    def __repr__(self):
        return str(self.queue)

    def __len__(self):
        return len(self.queue)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return Queue(self.queue[key])
        return self.queue[key]
