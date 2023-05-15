class Node:
    """ A node in a linked list. """

    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    """
    A linked list implementation.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def insert(self, value):
        """
        Inserts a new node with the given value at the end of the linked list.
        """
        # node = Node(value)
        # if self.head is None:
        #     self.head = node
        # else:
        #     current = self.head
        #     while current.next is not None:
        #         current = current.next
        #     current.next = node
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        """
        Searches for the node with the given value and returns True if found, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        """
        Returns a string representation of the linked list.
        """
        current = self.head
        string = ''
        while current is not None:
            string += f'{{ {current.value} }} -> '
            current = current.next
        string += 'NULL'
        return string

    def __str__(self):
        """
        Returns a string representation of the linked list using the to_string() method.
        """
        return self.to_string()

    def append(self, value):
        """
        Adds a new node with the given value to the end of the list.
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            return

    def insert_before(self, value, new_value):
        """insert new value before specific value"""
        node = Node(new_value)
        current = self.head
        if current is None:
            self.head = node
        elif current.value == value:
            node.next = current
            self.head = node
        else:
            while current.next is not None and current.next.value != value:
                current = current.next
            if current.next is None:
                current.next = node
            else:
                node.next = current.next
                current.next = node

    def insert_after(self, value, new_value):
        """insert new value after specific value"""
        node = Node(new_value)
        current = self.head
        if current is None:
            self.head = node
        else:
            while current is not None and current.value != value:
                current = current.next
            if current is None:
                current.next = node
            else:
                node.next = current.next
                current.next = node


    # def kth_from_end(self, k):
    #     """
    #     Returns the kth node from the end of the linked list.

    #     Args:
    #         k (int): The distance from the end of the linked list to the desired node.

    #     Returns:
    #         The value of the kth node from the end of the linked list, or None if k is negative or the linked list is empty.

    #     """

    #     if k < 0:
    #         return None
    #     if self.head is None:
    #         return None
    #     pointer1 = self.head
    #     pointer2 = self.head
    #     for i in range(k+1):
    #         if pointer2 is None:
    #             return None
    #         pointer2 = pointer2.next
    #     while pointer2:
    #         pointer1 = pointer1.next
    #         pointer2 = pointer2.next
    #     return pointer1.value
    
    def kth_from_end(self, k):
        """
        Returns the value of the node that is k positions from the end of the linked list.

        Args:
            k (int): The position from the end of the list (0-indexed).

        Returns:
            int: The value of the node at the kth position from the end of the list.

        Raises:
            ValueError: If k is a negative value or greater than or equal to the length of the list.
        """
        if k < 0:
            raise ValueError("Invalid value of k")

        pointer1 = self.head
        pointer2 = self.head

        # Move pointer2 k positions ahead
        for _ in range(k):
            if pointer2 is None:
                raise ValueError("Invalid value of k")
            pointer2 = pointer2.next

        # Check if pointer2 is None, indicating that k is equal to the length of the list
        if pointer2 is None:
            raise ValueError("Invalid value of k")

        # Move both pointers until pointer2 reaches the end of the list
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1.value


    @staticmethod
    def zip_lists(ll1, ll2):
        """
        Zips two linked lists together by alternating their nodes.

        Args:
            ll1 (LinkedList): The first linked list to be zipped.
            ll2 (LinkedList): The second linked list to be zipped.

        Returns:
            The head node of the zipped linked list.
        """

        if not ll1.head and not ll2.head:
            raise ValueError("Empty Lists!")
        if not ll1.head:
            return ll2
        if not ll2.head:
            return ll1

        current1, current2 = ll1.head, ll2.head
        while current1 and current2:
            next1, next2 = current1.next, current2.next
            current1.next = current2
            current2.next = next1

            current1, current2 = next1, next2

        return ll1
