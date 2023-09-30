#!/usr/bin/python3
"""write a class Node that defines a node of a singly linked list"""


class Node:
    """node class"""
    def __init__(self, data, next_node=None):
        """initalize a node

        Args:
            data(int): the data in the node
            next_node(Node): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets the next node in the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class that defines a single linked list"""

    def __init__(self):
        """initalizes the head of the list"""
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        data_list = []
        temp = self.__head
        while temp is not None:
            data_list.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(data_list)
