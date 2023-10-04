
from example_007_queue import Queue

class stack_adapter:

    def __init__(self):

        self.queue1 = Queue()

        self.queue2 = Queue()

 
    # O(N)
    def push(self, item):
        # put an item on top (front of the queue)
        self.queue2.enqueue(item) # add item to empty queue
        while not self.queue1.is_empty(): # for the whole list
            self.queue2.enqueue(self.queue1.dequeue()) # walk everybody to the new line

        while not self.queue2.is_empty(): # for the whole list
            self.queue1.enqueue(self.queue2.dequeue()) # walk everybody to original line but new guy is in front


 
    # O(C)
    def pop(self):
        # return and remove front of the line
        return self.queue1.dequeue()


 
    # O(N)
    def peek(self):
        # return the front of the line
        data = self.queue1.dequeue()

        self.push(data)

        return data
    

def main():

    data = [5, 20, 30, 4, 6, 24, 25, 19]

    stack = stack_adapter()

    for i in data:
        stack.push(i)

    print(f"the top value is {stack.pop()}")
    print(f"the top value is {stack.pop()}")
    print(f"the top value is {stack.pop()}")
    # stack.pop()
    stack.push(96)
    print(f"the top value is {stack.pop()}")
    stack.peek()

    print(stack)


if __name__ == "__main__":
    main()