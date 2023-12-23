# tree node learning

# 1.define tree
# 2.Add node
# 3.Build up tree

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = None

    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = data
                else:
                    self.left = Node(data) #if left has data and under of it has data it will use down node to consider
            elif data > self.data:
                if self.data is None:
                    self.right = data
                else:
                    self.right = Node(data) #if left has data and under of it has data it will use down node to consider

if __name__ == '__main__':    
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')

# 4. print all node in order 