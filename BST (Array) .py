class Tree:

    def __init__(self , arr):
        self.arr = arr
        self.n = len(arr)

    def empty(self):
        return self.arr == []

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
        self.inorder(2*idx+1)
        if self.arr[idx] != None:
            print(self.arr[idx],end= ' ')
        self.inorder(2*idx+2)

    def postorder(self , idx = 0):
        if idx >= self.n : return
        self.postorder(2*idx+1)
        self.postorder(2*idx+2)
        if self.arr[idx] != None:
            print(self.arr[idx],end= ' ')

a = [5,4,6,3,None,None,8,1,None,None,None,None,None,7,9,None,2]
tree = Tree(a)

print(tree.min_key())
print(tree.max_key())
print(tree.search(6))
print(tree.height())
print(tree.cnt_nodes())
print(tree.cnt_leaves())
print(tree.cnt_internals())
tree.preorder();print()
tree.inorder();print()
tree.postorder()
