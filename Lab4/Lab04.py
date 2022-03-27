"""
CIS 211 Spring 2021 Week 4 Lab 4

Author: Jacob Burke

Credits: N/A

Created a Node class, and two child classes Leaf and Internal. Used to demonstrate recursion
through inheritance.
"""


class Node:
    def __init__(self, node_data: int):
        self.node_data = node_data

    def sum_node_data(self) -> int:
        raise NotImplementedError("sum_node_data should be implemented in subclasses")

    def __str__(self):
        raise NotImplementedError()


class Leaf(Node):
    def __init__(self, node_data: int):
        super().__init__(node_data)
        self.node_data = node_data

    def sum_node_data(self) -> int:
        return self.node_data

    def __str__(self):
        return f"{self.node_data}"

class Internal(Node):
    def __init__(self, node_data: int, left: Node, right: Node):
        super().__init__(node_data)
        self.node_data = node_data
        self.left = left
        self.right = right

    def sum_node_data(self) -> int:
        return self.node_data + self.left.sum_node_data() + self.right.sum_node_data()

    def __str__(self):
        return f"<{self.node_data},{str(self.left)},{str(self.right)}>"


def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum_node_data())
    print(str(root))


if __name__ == '__main__':
    main()




