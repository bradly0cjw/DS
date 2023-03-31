def findkey(preorder, inorder):
    if not len(preorder) > 0:
        return []
    root = preorder[0]
    index = inorder.index(root)
    left = findkey(preorder[1:index+1], inorder[:index])
    right = findkey(preorder[index+1:], inorder[index+1:])
    return left + right + [root]

n = int(input())
for i in range(n):
    n = input().split()
    preorder = list(n[1])
    inorder = list(n[2])
    postorder = findkey(preorder, inorder)
    print("".join(postorder))
