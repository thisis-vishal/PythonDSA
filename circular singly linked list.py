class circularLinkedList:
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
    def createCLL(self,value):
        node=Node(value)
        node.next=node
        self.head=node
        self.tail=node
        return("successfully created")
    def insertionCSLL(self,value,location):
        if self.head==None:
            return "head is empty"
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==-1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                newNode.next=node.next
                node.next=newNode
    def traverse(self):
        if self.head==None:
            return "empty"
        node=self.head
        while node:
            print(node.value)
            node=node.next
            if node==self.tail.next:
                break
    def search(self,givenvalue):
        if self.head is None:
            return ("empty")
        else:
            index=0
            tempNode=self.head
            while tempNode:
                if (tempNode.value==givenvalue):
                    return(f"true at index {index}")
                tempNode=tempNode.next
                index+=1
                if tempNode==self.tail.next:
                    return("doesnt exits")
    def delteion(self,location):
        if self.head==None:
            return("No element ot delete")
        else:
            if location==0:
                self.head=self.head.next
                self.tail.next=self.head
            elif location==-1:
                node=self.head
                while node:
                    if node.next==self.tail:
                        break
                    node=node.next
                node.next=self.head
                self.tail=node
            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                nextNode=node.next
                node.next=nextNode.next
                                
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
newcll=circularLinkedList()
newcll.createCLL(1)
newcll.insertionCSLL(5,-1)
newcll.insertionCSLL(10,1)
newcll.insertionCSLL(2,0)
newcll.insertionCSLL(3,2)
print([node.value for node in newcll])
newcll.delteion(0)
print([node.value for node in newcll])
newcll.delteion(-1)
print([node.value for node in newcll])
newcll.delteion(1)
print([node.value for node in newcll])
