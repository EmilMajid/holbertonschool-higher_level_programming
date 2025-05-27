#!/usr/bin/python3
class MyList(list):
    """
    MyList class inherits from the built-in list class.
    It adds a public instance method called print_sorted.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order
        without modifying the original list.

        Notes:
            - All elements are assumed to be integers.
            - The original list remains unchanged.
        """
        print(sorted(self))
