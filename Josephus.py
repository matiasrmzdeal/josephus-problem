#  File: Josephus.py
#  Student Name: Matias Ramirez de Alva
#  Student UT EID: mr59342

import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        newNode = Link(data)
        if self.first == None:
            self.first = newNode
            self.last = newNode
            newNode.next = newNode
        else:
            newNode.next = self.first
            self.last.next = newNode
            self.last = newNode

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        if (self.first is None):
            return None
        current = self.first
        while True:
            if current.data == data:
                return current
            
            current = current.next
            

            if current.next == self.first:
                print("ISSUE TWO")
                return None

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        if (self.first is None):
            return None
        current = self.first
        previous = self.last
        while True:
            if current.data == data:
                previous.next = current.next
                #case of removed value being first, changing first pointer
                if current == self.first:
                    self.first = current.next
                #case of removed value being last, chaning last pointer
                if current == self.last:
                    self.last = previous
                return current
            previous = current
            current = current.next
            if current == self.first:
                return None

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        
        if (self.first is None):
            return None, None
        # find start node
        current = self.find(start)
        
        # take steps from start
        for st in range(step):
            previous = current
            current = current.next
        
        # call delete function / if doesn't work return None
        deleted_node = self.delete(current)
        successor = current.next
        # return deleted_node, successor
        return deleted_node, successor

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if self.first is None:
            return "List is Empty"
        
        items = []
        current = self.first
        while True:
            items.append(str(current.data))
            current = current.next

            if current == self.first:
                break
        return f"Circular List: {''.join(items)}"


# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    my_list = CircularList()
    for num in range(num_soldiers):
        my_list.insert(num+1)
    return my_list


# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    start = my_list.find(start_data)
    print(start)
    for i in range(num_soldiers):
        deleted_node, successor = my_list.delete_after(start, step_count)
        print(deleted_node, successor)
        start = successor


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()