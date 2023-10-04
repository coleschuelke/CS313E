
from example_008_linked_list import LinkedList

 

class stack_adapter2:

    def __init__(self):

        self.list=LinkedList()
        self.top_value = None




    # O(C)
    def push(self, item):

        # add to the front
        self.list.insert_first(item)
        # keep track of what should be on top
        self.top_value = item

    # O(C)
    def pop(self):

        # get head data and delete the first node
        # value = self.list.find_link(self.top_value)
        # self.list.delete_link(self.top_value)
        value = self.list.find_link(self.top_value).data
        self.list.delete_link(self.top_value).data
        self.top_value = self.list.first.data
        return value


    # O(C)
    def peek(self):

        # complete this method
        return self.list.find_link(self.top_value).data





def main():

    data = [5, 20, 30, 4, 6, 24, 25, 19]

    stack = stack_adapter2()

    for i in data:
        stack.push(i)

    print(f"the top value is {stack.pop()}")
    print(f"the top value is {stack.pop()}")
    print(f"the top value is {stack.pop()}")
    # stack.pop()
    stack.push(96)
    print(f"the top value is {stack.peek()}")


if __name__ == "__main__":
    main()