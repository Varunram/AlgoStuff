# AVL Tree - very very dangerous


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = data

    def __data__(self):
        return "%s" % (self.data)


class AVLTree():
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, data):
        n = Node(data)

        if self.node == None:
            self.node = n
            self.node.left = None
            self.node.right = None

        elif data < self.node.data:
            self.node.left.insert(data)
        elif data > self.node.data:
            self.node.right.insert(data)
        else:
            print "Key already exists in tree, won't insert"

        self.rebalance()

    def rebalance(self):
        self.update_heights(recursive=False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    # LR rotation
                    #     x               x
                    #    / \             / \
                    #   y   D           z   D
                    #  / \        ->   / \
                    # A   z           y   C
                    #    / \         / \
                    #   B   C       A   B

                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()
                # Left Left Case -> rotate z,x to the right
                #       x                 z
                #      / \              /   \
                #     z   D            y     x
                #    / \         ->   / \   / \
                #   y   C            A   B C   D
                #  / \
                # A   B
                self.rotate_right()
                self.update_balances()
                self.update_heights()

            if self.balance < -1:
                if self.node.right.balance < 0:
                    # RL rotation
                                        #     y               y
                    #    / \             / \
                    #   A   x           A   z
                    #      / \    ->       / \
                    #     z   D           B   x
                    #    / \                 / \
                    #   B   C               C   D
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()
                # Right Right Case -> rotate y,x to the left
                #       y                 z
                #      / \              /   \
                #     A   z            y     x
                #        / \     ->   / \   / \
                #       B   x        A   B C   D
                #          / \
                #         C   D
                self.rotate_left()
                self.update_balances()
                self.update_heights()

    def update_heights(self):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            self.height = 1 + max(self.node.left.height,
                                  self.node.right.height)
        else:
            self.height = -1

    def update_balances(self):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()
            self.balances += self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        # Left subtree root replaces current root
        new_root = self.node.left.node
        old_root = self.node
        new_left_sub = new_root.right.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        # Right subtree root replaces current root
        new_root = self.node.right.node
        old_root = self.node
        new_left_sub = new_root.left.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, data):
        if self.node != None:
            if self.node.data == data:
                self.node = None
            elif not self.node.left.node:
                self.node = self.node.right.node
            elif not self.node.right.node:
                self.node = self.node.left.node
            else:
                successor = self.node.left.node
                while successor:
                    successor = self.node.left.node

                if successor:
                    self.node.data = successor.data
                    self.node.right.delete(successor.data)

        elif data < self.node.data:
            self.node.left.delete(data)
        elif data > self.node.data:
            self.node.right.delete(data)

        self.rebalance()

    def inorder_traversal(self):
        result = []
        if not self.node:
            return result

        results.extends(self.node.left.inorder_traversal())
        results.append(node.data)
        results.extends(self.node.right.inorder_traversal())
        return result
