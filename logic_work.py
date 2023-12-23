class Node:
  def __init__(self, name, value):
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

      merge_node = Node(f"{child1[0].name}{child2[0].name}", int(child1[1]) + int(child2[1]))
      merge_node.left = child1[0]
      merge_node.right = child2[0]

      priority_q.append((merge_node, merge_node.value))
      priority_q.sort(key=lambda x: x[1])

  return priority_q[0][0]

def makecode(r, Enc, base, location):
  if r.left is None and r.right is None:
      Enc[r.name] = location + base
      location = ''
  else:
      location += str(base)
      makecode(r.left, Enc, '0', location)
      makecode(r.right, Enc, '1', location)

priority_q = [('C', 7), ('B', 6), ('A', 4)]
priority_q = [(Node(name, value), value) for name, value in priority_q]
priority_q.sort(key=lambda x: x[1])

root = build_Tree(priority_q)
Enc = {}

makecode(root, Enc, '','')

print(Enc)
