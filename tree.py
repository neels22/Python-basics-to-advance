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

def interative_preorder(node):

    stack=[]
    preorder=[]

    stack.append(node)

    while stack:
        root = stack.pop()
        if root:
            preorder.append(root.data)

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)


    return preorder

def iterative_inorder(node):

    stack = []
    inorder = []

    while True:

        while node:
            stack.append(node)
            node = node.left
        

        if not stack:
            break
        

        node = stack.pop()
        inorder.append(node.data)
        

        node = node.right

    return inorder

def iterative_postorder_2stack(root):
    if root is None:
        return []

    stack1 = []
    stack2 = []
    postorder = []

    # Start with root in the first stack
    stack1.append(root)

    # Traverse the tree
    while stack1:
        node = stack1.pop()
        stack2.append(node)

        # Push left and right children to stack1
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # Pop from stack2 to get the post-order traversal
    while stack2:
        postorder.append(stack2.pop().data)

    return postorder



def main():
    root = Node(10)
    values = [5, 15, 2, 7, 12, 20]
    for value in values:
        root = insert(root, value)
    
    print("In-order Traversal of the Binary Tree:")
    in_order_traversal(root)
    print()

    level_order_traversal(root)

    ans =interative_preorder(root)
    print("this is iterative", ans)
    ans =iterative_inorder(root)
    print("this is iterative", ans)
    ans =iterative_postorder_2stack(root)
    print("this is iterative", ans)



        



if __name__ == "__main__":
    main()
