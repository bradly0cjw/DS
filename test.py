class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.child = []
        self.leaf = leaf
    
    def insert_non_full(self, key):
        i = len(self.keys) - 1
        
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            if len(self.child[i + 1].keys) == 2 * t - 1:
                self.split_child(i + 1, self.child[i + 1])
                if key > self.keys[i + 1]:
                    i += 1
            self.child[i + 1].insert_non_full(key)
    
    def split_child(self, i, y):
        z = BTreeNode(leaf=y.leaf)
        self.child.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t - 1)]
        y.keys = y.keys[0: (t - 1)]
        
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]
    
    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and key == self.keys[i]:
            return self
        elif self.leaf:
            return None
        else:
            return self.child[i].search(key)
    
    def display(self, depth=0):
        prefix = '\t' * depth
        print(f"{prefix}{', '.join(str(k) for k in self.keys)}")
        if not self.leaf:
            for child in self.child:
                child.display(depth + 1)


class BTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = BTreeNode(leaf=True)
            self.root.keys.append(key)
        else:
            if len(self.root.keys) == (2 * t - 1):
                new_root = BTreeNode(leaf=False)
                new_root.child.append(self.root)
                self.root = new_root
                self.root.split_child(0, self.root.child[0])
            self.root.insert_non_full(key)
    
    def search(self, key):
        if self.root is None:
            return None
        else:
            return self.root.search(key)
    
    def display(self):
        if self.root is None:
            print("Empty B-tree")
        else:
            self.root.display()


# Usage
t = 3  # Order of the B-tree

tree = BTree()

# Inserting values into the B-tree
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(6)
tree.insert(12)
tree.insert(30)

# Display the B-tree structure
tree.display()

# Search for a key in the B-tree
result = tree.search(12)
if result is not None:
    print("Key found in the B-tree!")
else:
    print("Key not found in the B-tree.")
