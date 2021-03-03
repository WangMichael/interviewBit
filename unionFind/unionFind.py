class UnionFind:

    def __init__(self, count):
        self.count = count
        self.bucket = [i for i in range(count)]


    def union(self, a, b):

        root_a  = self.find(a)
        root_b  = self.find(b)

        if root_a != root_b:
            self.bucket[root_a] = root_b
            self.count -= 1


    def isConnected(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b


    def find(self, a):

        while a != self.bucket[a]:
            self.bucket[a] = self.bucket[self.bucket[a]]
            a = self.bucket[a]

        return a
