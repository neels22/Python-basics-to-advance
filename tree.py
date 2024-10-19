class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node




def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def level_order_traversal(node):
    ansarr = []
    queue = []
    queue.append(node)

    while queue:
        size = len(queue)
        level = []

        while size:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(node.data)
            size -= 1
        ansarr.append(level)

    print(ansarr)





def main():
    root = Node(10)
    values = [5, 15, 2, 7, 12, 20]
    for value in values:
        root = insert(root, value)
    
    print("In-order Traversal of the Binary Tree:")
    in_order_traversal(root)
    print()

    level_order_traversal(root)


if __name__ == "__main__":
    main()
