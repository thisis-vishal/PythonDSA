class circularDoublyLinkedList:
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
    def createCDLL(self,value):
        node=Node(value)
        node.next=node
        node.prev=node
        self.head=node
        self.tail=node
        return("successfully created")
    def insertion (self,value,location):
        if self.head==None:
            return "List is empty"
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.tail.next=newNode
                self.head=newNode
            elif location==-1:
                newNode.next=self.head
                newNode.prev=self.tail
                self.tail.next=newNode
                self.head.prev=newNode
                self.tail=newNode
            else:
                index=0
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
            node=self.head
            while node:
                print(node.value,end=" ")
                if node.next==self.head:
                    print("")
                    break
                node=node.next
    def reverseTraversal(self):
        if self.head==None:
            return "List is empty"
        else:
            node=self.tail
            while node:
                print(node.value,end=" ")
                if node.prev==self.tail:
                    print("")
                    break
                node=node.prev
    def search(self,value):
        if self.head==None:
            return "List is empty"
        else:
            node=self.head
            index=0
            while node:
                if node.value==value:
                    print(f"given value is at index {index}")
                if node.next==self.head:
                    break
                node=node.next
                index+=1    
    def deletion(self,location):
        if self.head==None:
            return "List is empty"
        else:
            if location==0:
                self.head.next.prev=self.tail
                self.tail.next=self.head.next
                self.head=self.head.next
            elif location == -1:
                self.tail.prev.next=self.head
                self.tail=self.tail.prev
                self.head.prev=self.tail
            else:
                index=0
                tempNode=self.head
                while index<location-1:
                    index+=1
                    tempNode=tempNode.next
                tempNode.next=tempNode.next.next
                tempNode.next.next.prev=tempNode
    def deleteEntire(self):
        if self.head==None:
            return "List is empty"
        else:
            self.tail.next=None
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
newCDll=circularDoublyLinkedList()
newCDll.createCDLL(2)
newCDll.insertion(5,0)
newCDll.insertion(6,-1)
newCDll.insertion(8,1)
newCDll.traversal()
newCDll.deletion(3)
newCDll.traversal()
