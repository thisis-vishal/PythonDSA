class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insertSLL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if (location==0):
                newNode.next=self.head
                self.head=newNode
            elif (location== -1):
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
                if tempNode==self.tail:
                    self.tail=newNode
    def traverse(self):
        if (self.head==None):
            print("No item in list")
        else:
            node=self.head
            while node!=None:
                print(node.value)
                node=node.next
    def search(self,value):
        node=self.head
        if node==None:
            print("There is no items in list")        
        else:
            index=0
            find=False
            while node!=None:
                if node.value==value:
                    find=True
                    break
                else:
                    index+=1
                node=node.next
            if(find):
                print(index)
            else:
                print("Element is not in the list")
    def delete(self,location):
        node=self.head
        if node==None:
            return("No element is in the list")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head,self.tail=None
                else:
                   self.head=self.head.next       
            elif location==-1:
                if self.head==self.tail:
                    self.head,self.tail=None
                else:
                    while node!=None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=node
            else:
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
newsl=SinglyLinkedList()
Node1=Node(5)
newsl.head=Node1
newsl.tail=Node1
newsl.insertSLL(2,0)
newsl.insertSLL(6,1)
newsl.insertSLL(10,-1)
newsl.traverse()
newsl.delete(1)
newsl.traverse()
