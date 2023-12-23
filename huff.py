# huffman

def priority_queue(freq_dict):
    priority_queue = list(freq_dict.items())
    priority_queue.sort(key=lambda x: x[1])
    return priority_queue

class Node:
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

def Create_Tree(priority_q):
    while len(priority_q) > 1:
        child1 = priority_q.pop(0)
        child2 = priority_q.pop(0)

        merge_node = Node(f"{child1[0]}{child2[0]}",int(child1[1]) + int(child2[1]))
        merge_node.left = child1
        merge_node.right = child2

        priority_q.append((merge_node,merge_node.value))
        priority_q.sort(key=lambda x: x[1])
        # print(priority_q)
        # print('\n')
    return priority_q

input_data = "AAAAABBBBCCC"

freq = {}
for c in input_data:
    if c in freq:
        freq[c] += 1
    else: 
        freq[c] = 1
# print(freq)

priority = priority_queue(freq)
# print(priority)

root = Create_Tree(priority) #This is a Huffman's tree
