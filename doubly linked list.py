class doublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next==self.head:
                break
            node=node.next
    def createDLL(self,value):
        node=Node(value)
        node.next=None
        node.prev=None
        self.head=node
        self.tail=node
        return("successfully created")
    def insertion(self,value,location):
        if self.head==None:
            return "List is empty"
        else:
            newNode=Node(value)
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            elif location==-1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else:
                index = 0
                tempNode=self.head
                while index<location-1:
                    index+=1
                    tempNode=tempNode.next
                newNode.next=tempNode.next
                newNode.prev=tempNode
                tempNode.next.prev=newNode
                tempNode.next=newNode
    def traversal(self):
        if self.head==None:
            return "List is empty"
        else:
            currentNode=self.head
            while currentNode != None:
                print(currentNode.value,end=" ")
                if currentNode.next==None:
                    print("")
                currentNode=currentNode.next
    def reverseTraversal(self):
        if self.head==None:
            return "List is empty"
        else:
            currentNode=self.tail
            while currentNode != None:
                print(currentNode.value,end=" ")
                if currentNode.prev==None:
                    print("")
                currentNode=currentNode.prev
    def search(self,value):
        if self.head==None:
            return "List is Empty"
        else:
            index=0
            node=self.head
            while node:
                if node.value==value:
                    print(f"Element present at index {index}")
                index+=1
                node=node.next
    def deletion(self,location):
        if self.head==None:
            return "list is empty"
        else:
            if location==0:
                self.head=self.head.next
                self.head.prev=None
            elif location==-1:
                self.tail=self.tail.prev
                self.tail.next=None
            else:
                curNode=self.head
                index=0
                while index<location-1:
                    curNode=curNode.next
                    index+=1
                curNode.next=curNode.next.next
                curNode.next.prev=curNode
    def deleteWhole(self):
        tempNode=self.head
        while tempNode:
            tempNode.prev=None
            tempNode=tempNode.next
        self.head=None
        self.tail=None
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
newDll=doublyLinkedList()
newDll.createDLL(1)
newDll.insertion(2,0)
newDll.insertion(5,-1)
newDll.insertion(6,1)
newDll.insertion(7,2)
newDll.traversal()
newDll.reverseTraversal()
newDll.search(7)
newDll.deletion(2)
print([node.value for node in newDll])
