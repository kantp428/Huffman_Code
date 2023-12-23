
class Node:
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

priority_q = [('C', 3), ('B', 4), ('A', 5), ('M', 4), ('Q', 5)]


while len(priority_q) > 1:
        child1 = priority_q.pop(0)
        child2 = priority_q.pop(0)

        merge_node = Node(f"{child1[0]}{child2[0]}",int(child1[1]) + int(child2[1]))
        merge_node.left = child1
        merge_node.right = child2

        priority_q.append((merge_node,merge_node.value))
        priority_q.sort(key=lambda x: x[1])
        print(priority_q)
        print('\n')
