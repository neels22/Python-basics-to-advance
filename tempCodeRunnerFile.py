            preorder.append(root.data)

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)