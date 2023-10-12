"""
  File: josephus.py
  Description: an implementation of the josephus problem

  Student Name: Quentin Schuelke
  Student UT EID: qcs86 

  Partner Name: n/a
  Partner UT EID: n/a

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 09/11/23
  Date Last Modified: 09//23
"""


import sys
class Link(object):
    ''' This class represents a link between data items only.'''
    def __init__ (self, data, next_link = None):
        self.data = data
        self.next = next_link

    def print_data(self):
        ''' Print the data contained in this link.'''
        print(self.data)

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        if self.first is None:
            self.first = new_link
            self.last = new_link
            new_link.next = new_link
        else:
            new_link.next = self.first
            self.first = new_link
            self.last.next = new_link

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.first
        # should never be the case in a circle, which it isn't
        if current.next is None:
            return None
        
        while current.data != data:
            # shouldbt happen
            if current is None:
                return None
            
            current = current.next
        return current


    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        '''Removes the data from the list if exist and fix the link problems.'''

        current = self.first
        previous = self.first

        # supposed to handle the case of an empty list but I'm not sure it's working
        if current is None:
            return None
        
        while current.data != data:
            print("we are in the while loop")
            if current.next is None:
                return None

            # step along the links
            previous = current
            current = current.next

            # went thru the whole circle and didn't find it
            if current == self.first:
                return None

        if current == self.first:
            if current == current.next:
                self.first = None
                return current
            else:
                self.first = self.first.next
        else:
            # connect the nodes on each side of the deleted link
            previous.next = current.next

        return current

        

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        current = start

        if current is None:
            return None

        for i in range(n-1):
            previous = current
            current = current.next
            # print("we won't kill him yet (but his time will come)")

        # delete the link by linking the previous one to the next one, skipping the current one
        if previous.next == current.next:
            return (current, None)
        else:
            previous.next = current.next

        return (current, current.next) # deleted, next link after deleted (dtype = Node)


        

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__ (self):
        if not self.first:
            return str([])
        list_format = []
        list_format.append(self.first.data)
        current = self.first.next
        while current != self.first:
            list_format.append(current.data)
            current = current.next

        list_format.reverse()

        return str(list_format)



def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)
    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)
    
    # your code
    linked_list = CircularList()
    for i in range(num_soldiers):
        linked_list.insert(num_soldiers-i)

    # if linked_list.first == None:
    #     print("You are not even filling the list, dumbass. Fix your insert function")
    # else:
    #     print("At least your insert kinda works but there are more problems somewhere else")

    # print(type(linked_list.first))
    # print(type(linked_list.first.data))


    # # first delete call
    start_node = linked_list.find(start_count)
    deleted_link, next_link = linked_list.delete_after(start_node, elim_num)
    print(deleted_link.data)
    # test = linked_list.find(0)

    while next_link is not None:
        deleted_link, next_link = linked_list.delete_after(next_link, elim_num)
        print(deleted_link.data)
    # circ = CircularList()
    # # # for i in range(10):
    # # #     circ.insert(i)
    # circ.insert(1)
    # # print(circ)
    # # print(str(circ))
    # circ.delete(1)
    # print(circ)
    # # print(circ.first.data)


if __name__ == "__main__":
    main()
