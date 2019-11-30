class TreeNode:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, key):
        if not self.key:
            self.key = key
        elif key < self.key:
            if not self.left:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if not self.right:
                self.right = TreeNode(key)
            self.right.insert(key)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.key)
        if self.right:
            self.right.printTree()

    def delMin(self):
        if not self.left:
            return self.right if self.right else TreeNode()
        if self.left.left:
            tree = self.left
        else:
            self.left = self.left.right
            return self
        while (tree.left.left):
            tree = tree.left
        if tree.left.right:
            tree.left.key = tree.left.right.key
            tree.left.left = tree.left.right.left
            tree.left.right = tree.left.right.right
        else:
            tree.left = None
        return self

    def delMax(self):
        if not self.right:
            return self.left if self.left else TreeNode()
        if self.right.right:
            tree = self.right
        else:
            self.right = self.right.left
            return self
        while (tree.right.right):
            tree = tree.right
        if tree.right.left:
            tree.right.key = tree.right.left.key
            tree.right.right = tree.right.left.right
            tree.right.left = tree.right.left.left
        else:
            tree.right = None
        return self
        
        

if __name__ == "__main__":
    tree = TreeNode()
    tree.insert(60)
    tree.insert(58)
    tree.insert(14)
    tree.insert(9)
    tree.insert(3)
    tree.insert(5)
    tree.insert(65)
    tree.insert(72)
    tree.insert(67)
    tree.insert(9)
    tree.insert(9)
    #tree.PrintTree()