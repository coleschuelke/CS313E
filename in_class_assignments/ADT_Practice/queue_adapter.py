from example_006_stack import Stack

class queue_adapter:

    def __init__(self):

        self.stack1 = Stack()
        self.stack2 = Stack()


    # O(N)
    def enqueue(self, item):
        # put something at the bottom of the stack
        while not self.stack1.is_empty(): # for the whole left stack
            # move everything to right stack
            self.stack2.push(self.stack1.pop()) # order will be reversed 

        self.stack1.push(item)

        while not self.stack2.is_empty():
            # move it all back to the left stack 
            self.stack1.push(self.stack2.pop()) # everything is back to normal with an extra item at the bottom

    # O(C)
    def dequeue(self):
        # grab something from the top of the stack 
        return self.stack1.pop()


def main():

    data = [5, 20, 30, 4, 6, 24, 25, 19]

    queue = queue_adapter()

    for i in data:
        queue.enqueue(i)

    print(f"dequeueing {queue.dequeue()}")
    print(f"dequeueing {queue.dequeue()}")
    queue.enqueue(15)

    print(f"dequeueing {queue.dequeue()}")
    


if __name__ == "__main__":
    main()