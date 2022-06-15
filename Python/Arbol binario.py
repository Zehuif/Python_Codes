class bst_node(object):
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class bst(object):
    def __init__(self, root = None):
        self.root = root
    
    def empty(self):
        return self.root == None

    def insert(self, value):
        if(self.empty()):
            self.root = bst_node(value, None, None)
            return
        aux = self.root
        while(aux != None):
            if(aux.value >= value):
                if(aux.left == None):
                    aux.left = bst_node(value)#no hay que poner none left y right?
                    return
                aux = aux.left
            else:
                if(aux.right == None):
                    aux.right = bst_node(value)
                    return
                aux = aux.right

    def preorder(self, node):
        if(node == None):
            return
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)
    
    def search(self, key):#1 para cuando encuentra, 0 para cuando no.
        aux = self.root
        while(aux != None):
            if(aux.value == key):
                return 1
            elif(aux.value > key):
                aux = aux.left
            else:
                aux = aux.right
        return 0

if __name__ == "__main__":
    tree = bst()
    tree.insert(5)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)
    tree.insert(0)
    tree.insert(6)
    tree.insert(51)
    #tree.preorder(tree.root)
    print(tree.search(5))
    print(tree.search(51))
    print(tree.search(71))
