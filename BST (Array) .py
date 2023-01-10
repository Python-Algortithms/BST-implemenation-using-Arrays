class Tree:

    def __init__(self):
        self.arr = [None]*50
        self.n = len(self.arr)

    def empty(self):
        return self.arr == []

    def insert(self,idx,c,key):
        if c == 'l':
            self.arr[2*idx+1] = key
        elif c == 'r':
            self.arr[2*idx+2] = key

    def insert_root(self , key):
        self.arr [0] = key

    def search (self , key):

        if self.empty():
            print("Tree is empty !")
            return

        idx = 0
        while True:
            if idx < self.n :
                if self.arr[idx] != None:
                    if key < self.arr[idx]:
                        idx = 2*idx + 1
                    elif key > self.arr[idx]:
                        idx = 2*idx + 2
                    else:
                        return 1
                else:
                    return 0
            else:
                return 0

    def min_key(self):
        if self.empty():
            print("Tree is empty !")
            return

        idx = 0
        mn = self.arr [0]
        while True:
            if idx < self.n:
                if self.arr [idx] != None:
                    mn = self.arr[idx]
                    idx = 2 * idx + 1
                else:
                    return mn
            else:
                return mn

    def max_key(self):

        if self.empty():
            print("Tree is empty !")
            return

        idx = 0
        mx = self.arr [0]
        while True:
            if idx < self.n:
                if self.arr [idx] != None:
                    mx = self.arr[idx]
                    idx = 2 * idx + 2
                else:
                    return mx
            else:
                return mx

    def height(self , idx = 0):
        if idx >= self.n :return -1
        if self.arr[idx] == None:return -1
        return 1 + max(self.height(2*idx+1),self.height(2*idx+2))

    def cnt_nodes(self , idx = 0):
        if idx >= self.n :return 0
        if self.arr[idx] == None:return 0
        return 1 + self.cnt_nodes(2*idx+1)+self.cnt_nodes(2*idx+2)

    def cnt_leaves(self , idx = 0):

        idx = ans = 0

        while idx < self.n:
            f = 0
            if self.arr[idx] != None:
                if 2*idx+1 < self.n:
                    if self.arr[2*idx+1] == None:
                        f+=1
                else:
                    ans+=1

                if 2*idx+2 < self.n:
                    if self.arr[2*idx+2] == None:
                        f+=1

            if f == 2:ans+=1
            idx+=1

        return ans

    def cnt_internals(self , idx = 0):

        idx = ans = 0
        while idx<self.n:
            f = 0
            if 2*idx+1 < self.n:
                if self.arr [2*idx+1] != None:
                    f+=1

            if 2*idx+2 < self.n:
                if self.arr [2*idx+2] != None:
                    f+=1

            if f :ans+=1
            idx += 1

        return ans

    def preorder(self , idx = 0):
        if idx >= self.n : return
        if self.arr[idx] != None:
            print(self.arr[idx],end= ' ')
            self.preorder(2*idx+1)
            self.preorder(2*idx+2)

    def inorder(self , idx = 0):
        if idx >= self.n : return
        if self.arr[idx] != None:
            self.inorder(2*idx+1)
            print(self.arr[idx],end= ' ')
            self.inorder(2*idx+2)

    def postorder(self , idx = 0):
        if idx >= self.n : return
        if self.arr[idx] != None:
            self.postorder(2*idx+1)
            self.postorder(2*idx+2)
            print(self.arr[idx],end= ' ')

BST = Tree()

BST.insert_root(5)
BST.insert(0,'l',4)
BST.insert(0,'r',6)
BST.insert(1,'l',3)
BST.insert(2,'r',8)
BST.insert(3,'l',1)
BST.insert(6,'l',7)
BST.insert(6,'r',9)
BST.insert(7,'r',2)


print(BST.min_key())
print(BST.max_key())
print(BST.search(6))
print(BST.height())
print(BST.cnt_nodes())
print(BST.cnt_leaves())
print(BST.cnt_internals())


BST.preorder();print()
BST.inorder();print()
BST.postorder()
