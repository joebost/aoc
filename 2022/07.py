from utils.api import get_input

input_str = get_input(7)

class Node:
  def __init__(self, name, parent = None):
    self.name = name
    self.parent = parent
    self.child = []
  
  def append(self, name):
    self.child.append(Node(name=name, parent=self))

  def get_child(self, name):
    return [c for c in self.child if c.name == name][0]

head = Node("/")
file_to_size = {}

cd = head
for line in input_str.split("\n"):
  split = line.split(" ")
  if line == "$ cd /":
    cd = head
  elif line == "$ cd ..":
    cd = cd.parent
  elif line == "$ ls":
    continue
  elif "$ cd " in line:
    # "$ cd dir_name"
    dir_name = line.split(" ")[2]
    cd = cd.get_child(dir_name)
  elif split[0] == "dir":
    cd.append(line.split(" ")[1])
  else:
      size, name = line.split(" ")
      file_to_size[name] = int(size)
      cd.append(name=name)

def sum_under_node(node):
  if node.child == []:
    return file_to_size[node.name]
  else:
    sum_under = sum([sum_under_node(child) for child in node.child])
    node.size = sum_under
    return sum_under

sum_under_node(head)

def traverse(node):
  global summ
  if node.child == []:
    return

  [traverse(child) for child in node.child]
  
  summ += node.size if node.size < 100000 else 0

summ = 0
traverse(head)
print(summ)

def parse(puzzle_input):
    """Parse input."""
    terminal = puzzle_input.strip().split("\n")
    head = None
    curr_node = None

    for action in terminal:
        match action.split(" "):
            case '$', 'cd', directory:
                if directory == '..':
                    curr_node = curr_node.parent
                elif directory == '/':
                    head = Node()
                    head.name = directory
                    curr_node = head
                else:
                    next_node = [child for child in curr_node.children if child.name == directory]
                    curr_node = next_node[0]
            case '$', 'ls':
                continue
            case 'dir', directory:
                new_node = Node()
                new_node.name = directory
                new_node.parent = curr_node
                curr_node.children.append(new_node)
            case size, file:
                new_node = Node()
                new_node.children = None
                new_node.name = file
                new_node.size = int(size)
                new_node.parent = curr_node
                curr_node.children.append(new_node)

parse(input_str)
sum