from sympy import root
import QueueLinkedList as queue
class treeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
newBT=treeNode("Drinks")
leftChild=treeNode("Hot")
rightChild=treeNode("Cold")
tea=treeNode("Tea")
coffee=treeNode("Coffee")
leftChild.left=tea
leftChild.right=coffee
newBT.left=leftChild
newBT.right=rightChild
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if(root.value.left is not None): 
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
def search(rootNode,value):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==value:
                return "Success"
            if(root.value.left is not None): 
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
        return "Not found"
def insert (rootNode,value):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.left == None:
                newNode=treeNode(value)
                root.value.left=newNode
                return "Success"
            elif root.value.right == None:
                newNode=treeNode(value)
                root.value.right=newNode
                return "Success"
            else:
                if(root.value.left is not None): 
                    customQueue.enqueue(root.value.left)
                if(root.value.right is not None):
                    customQueue.enqueue(root.value.right)
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if(root.value.left is not None): 
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
        deepestNode=root.value
        return deepestNode
def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value==dNode:
                root.value=None
                return
            if root.value.right:
                if root.value.right is dNode:
                    root.value.right =None
                    return
                else:
                    customQueue.enqueue(root.value.right)
            if root.value.left:
                if root.value.left is dNode:
                    root.value.left =None
                    return
                else:
                    customQueue.enqueue(root.value.left)
            if(root.value.left is not None): 
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
def deleteNode(rootNode,node):
    if not rootNode:
        return "the bt doesnt exist"
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value.data==node:
                dNode=getDeepestNode(rootNode)
                root.value.data=dNode.data
                deleteDeepestNode(rootNode,dNode)
                return "Node deleted Successfully"
            if(root.value.left is not None): 
                customQueue.enqueue(root.value.left)
            if(root.value.right is not None):
                customQueue.enqueue(root.value.right)
        return "Node not found"
def deleteBinaryTree(rootNode):
    rootNode.data=None
    rootNode.left=None
    rootNode.right=None
    return "The BT has been deleted successfully"
# preOrderTraversal(newBT)
# inOrderTraversal(newBT)
# postOrderTraversal(newBT)
# levelOrderTraversal(newBT)
# print(search(newBT,"Coffese"))
# insert(newBT,"Alcholic")
# insert(newBT,"NonAlcoholic")
# levelOrderTraversal(newBT)
# deepestNode=getDeepestNode(newBT)
# print(deepestNode.data)
levelOrderTraversal(newBT)
deleteBinaryTree(newBT)
levelOrderTraversal(newBT)