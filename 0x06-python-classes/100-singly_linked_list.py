#!/usr/bin/python3
"""Node class that defines a node of a singly linked list"""

class Node:
    """class that defines a node of a singly linked list"""
    
    def __init__(self, data, next_node=None):
        """Instantiation function

        Args:
            data: data contained by the node
            next_node: next node

        Returns:
            nth
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not (next_node == None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter function to retrieve the value of __data

        Args:

        Returns:
            The value of __data
        """
        return self.__data
    
    @data.setter
    def data(self, value):
        """Setter function to set/change the value of __data

        Args:
            value: new value for __data

        Returns:
            Nth
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """Getter function to retrieve the value of __next_node

        Args:

        Returns:
            The value of __next_node
        """
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """Setter function to set/change the value of __next_node

        Args:
            value: new value for __next_node

        Returns:
            Nth
        """
        if not (value == None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""SinglyLinkedList class that defines a singly linked list"""

class SinglyLinkedList:
    """Class that defines a singly linked list"""
    
    def __init__(self):
        """Instantiation function

        Args:

        Returns:
            nth
        """
        self.__head = []
    
    def sorted_insert(self, value):
        """Function  that inserts a new Node
        into the correct sorted position in the list
        (increasing order)
        
        Args:
            Value: value of new node to be added
        
        Returns:
            nth
        """
        new_node = Node(data=value)
        self.__head.append(new_node)
    
    def __str__(self):
        """Function to print the singly linked list"""
        node_values = []
        for node in self.__head:
            node_values.append(node.data)
        node_values.sort()
        nodes_str = ""
        for i in node_values:
            if node_values.index(i) == 0:
                nodes_str = nodes_str + str(i)
            else:
                nodes_str = nodes_str + "\n" + str(i)
        
        return nodes_str
        
