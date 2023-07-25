class Node:
    def __init__(self):
        self.right = None
        self.left = None

    def max_depth(self):
        if not self:
            return 0
        else:
            left_depth = self.left.max_depth() if self.left else 0
            right_depth = self.right.max_depth() if self.right else 0
            return max(left_depth, right_depth) + 1


# Construct the tree
root = Node()
root.left = Node()
root.right = Node()
root.right.right = Node()

# Call the max_depth method on the root node
depth = root.max_depth()
print("Maximum depth of the tree:", depth)
