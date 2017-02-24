"""
升序单链表
Introduction: Construct a sorted singly linked list, which supports insert, remove, isEmpty, top and bot.
__author__ = v1siuol
__date = 2017.2.23
"""


class SortedSinglyLinkedList:
    """
    A singly linked list sorted in increasing order
    """
    class Node:  # element
        __slots__ = "_value", "_next"

        def __init__(self, v, n):
            self._value = v
            self._next = n

    def __init__(self):
        """
        Initialized empty linked list
        """
        self._head = self._tail = None
        self._size = 0

    def __iter__(self):
        """
        An iterator generator to visit the values in sequence
        """
        current = self._head
        while current is not None:
            yield str(current._value)
            current = current._next

    def __str__(self):
        """
        Names the endpoint values and lists all of them
        """
        if self.is_empty():
            return ""
        return " ".join(list(iter(self)))

    def __len__(self):
        return self._size

    def insert(self, value):
        """
        Insert a new value into the list, in sorted order
        """
        if self.is_empty():  # no element in linked list
            self._tail = self._head = self.Node(value, None)
        else:
            if value <= self._head._value:
                self._head = self.Node(value, self._head)
            elif value >= self._tail._value:
                self._tail._next = self.Node(value, None)
                self._tail = self._tail._next
            else:
                current = self._head
                while current._next._value <= value:
                    current = current._next
                current._next = self.Node(value, current._next)
        self._size += 1

    def remove(self,value):
        """
        Remove one occurrence of the given value from the list
        """
        if self.is_empty():
            #raise IndexError
            return
        current = self._head
        if current._value == value:
            self._head = self._head._next
        else:
            while current._next._value != value:
                current = current._next
                if current._next is None:  # remove value not found
                    return
            current._next = current._next._next
            if current._next is None:
                self._tail = current
        self._size -= 1

    def is_empty(self):
        """
        Determine whether the linked list is empty or not and return the boolean value
        """
        return self._size == 0

    def top(self):
        """
        Return the smallest value in the linked list
        """
        if self.is_empty():
            return None
        return self._head._value

    def bot(self):
        """
        Return the largest value in the linked list
        """
        if self.is_empty():
            return None
        return self._tail._value

# ----------------------test case----------------------------------

if __name__ == "__main__":
    if False:
        single = SortedSinglyLinkedList()
        print("top is", single.top())
        single.insert(1)
        print("list:", single)
        single.insert(2)
        print("list:", single)
        print("bot is", single.bot())
        single.remove(4)
        print("list:", single)
        single.remove(2)
        print("list:", single)
        single.insert(1)
        print("list:", single)
        single.remove(1)
        print("list:", single)
        for i in [2, 0, 6, 9, 4, 7, 1]:
            single.insert(i)
            print("Insert", i, ":", single)
        for i in [4, 6, 2, 0, 1, 9, 7]:
            single.remove(i)
            print("Remove", i, ":", single)
