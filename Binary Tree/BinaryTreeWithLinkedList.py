'''
Demonstrating Traversals
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


newBinaryTree = TreeNode('Drinks')
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')

leftToLeft = TreeNode('Tea')
rightToLeft = TreeNode('Coffee')
leftToRight = TreeNode('Thumps Up')
rightToRight = TreeNode('Wine')

newBinaryTree.left = leftChild
newBinaryTree.right = rightChild

leftChild.left = leftToLeft
leftChild.right = rightToLeft
rightChild.left = leftToRight
rightChild.right = rightToRight


def preOrderTraversal(root):
    if not root:
        return
    else:
        print(root.data)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)


def inOrderTraversal(root):
    if not root:
        return
    else:
        inOrderTraversal(root.left)
        print(root.data)
        inOrderTraversal(root.right)


def postOrderTraversal(root):
    if not root:
        return
    else:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.data)


def levelOrderTraversal(root):
    if not root:
        return
    else:
        # create queue using linked list then import that here in this program as per instructor
        # but let me at least try other methods
        pass


# preOrderTraversal(newBinaryTree)
# inOrderTraversal(newBinaryTree)
postOrderTraversal(newBinaryTree)
