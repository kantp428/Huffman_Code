
class Node:
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.left = None
        self.right = None    
    def __str__(self):
        return f"{self.name}"

def build_Tree(priority_q):
    while len(priority_q) > 1:
            child1 = priority_q.pop(0)
            child2 = priority_q.pop(0)

            merge_node = Node(f"{child1[0]}{child2[0]}",int(child1[1]) + int(child2[1]))
            merge_node.left = child1[0]
            merge_node.right = child2[0]
            # print(merge_node.name)

            priority_q.append((merge_node,merge_node.value))
            priority_q.sort(key=lambda x: x[1])
            # print(priority_q)
            # print('\n')
    return priority_q[0][0]

priority_q = [('C', 9), ('B', 6), ('A', 3), ('M', 2)]
priority_q.sort(key=lambda x: x[1])
# print(priority_q)
# print('\n')

root = build_Tree(priority_q)

left_child = root.left
right_child = root.right

def encode(root_data):
    Enc = {}
    if root_data.left and root_data.right is None:
         