class treeNode:
    def __init__(self,data=None,children=[]):
        self.data=data
        self.children=children
    def __str__(self,level=0):
        ret =" "*level +str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    def addChild(self,treeNode):
        self.children.append(treeNode)
tree=treeNode('Drinks',[])
cold=treeNode('Cold',[])
hot=treeNode('Hot',[])
cofee=treeNode('Cofee',[])
tea=treeNode('Tea')
alcoholic=treeNode("Alcoholic")
nonAlcoholic=treeNode("Non Alcoholic")
tree.addChild(cold)
tree.addChild(hot)
cold.addChild(alcoholic)
cold.addChild(nonAlcoholic)
hot.addChild(tea)
hot.addChild(cofee)
print(tree)