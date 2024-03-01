from binary_node import BinaryNode

n1 = BinaryNode(value='A')
n2 = BinaryNode(value='B')
n3 = BinaryNode(value='C', left=n1, right=n2)
n4 = BinaryNode(value='D')
n5 = BinaryNode(value='E')
n6 = BinaryNode(value='F', left=n4, right=n5)
n7 = BinaryNode(value='G', left=n3, right=n6)

graph = n7

'''
Implement Breadth First Search
1. First, check if the root node is the target. If it is, return the root node.
2. Otherwise, add the children of the current node to the **queue** of nodes.
3. Pop each from the queue and check if each are the target.
4. Return if target. Otherwise, go to step 2 and repeat.
'''
def bfs(graph, target_value):
    queue = [graph]
    while queue:
        current_node = queue.pop(0)
        if current_node.value == target_value:
            return current_node
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return None

# Pass these tests
assert bfs(graph, 'G').value == 'G'
assert bfs(graph, 'C').left.value == 'A'
assert bfs(graph, 'F').right.value == 'E'
assert bfs(graph, 'E').left == None
