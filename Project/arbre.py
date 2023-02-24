class BinaryTree:
    def __init__(self, l):
        self.val = l[0]
        if len(l) == 0:
            self.val = None
            self.left = None
            self.right = None
        else:
            self.val = l[0]
            self.left = BinaryTree(l[1])
            self.right = BinaryTree(l[2])

    def is_terminal(self):
        return (self.val is None)

    def __str__(self):
        if self.is_terminal():
            return ''
        else:
            s = str(self.val)
            if self.left is not None:
                s = s + str(self.left)
            if self.right is not None:
                s = s + str(self.right)
            return s
if __name__=="__main__":
    bt = BinaryTree([1, [2, [4,[],[5,[],[]] ] ,[] ], [3,[],[]]])
    print(bt)