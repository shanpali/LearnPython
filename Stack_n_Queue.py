class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def print(self):
        if len(self.stack) < 1:
            print("Stack is empty")
        else:
            print(self.stack)



class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def print(self):
        if len(self.queue) < 1:
            print("Queue is empty")
        else:
            print(self.queue)


print("====================stack======================")
st=Stack()
st.push(1)
st.push(2)
st.push(3)
print("Stack size= "+str(st.size()))
st.print()
st.pop()
st.print()
print("Stack size= "+str(st.size()))
print("====================stack end ======================")

print("====================Queue======================")

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print()
print("Queue size= "+str(q.size()))
q.dequeue()
q.print()
print("Queue size= "+str(q.size()))