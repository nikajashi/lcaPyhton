import unittest
import lca

class TestLca(unittest.TestCase):
    
    #checks if findLCA works for negative numbers
    def test_non_positive(self):
        self.root  = lca.Node(-1)
        self.root.left = lca.Node(-2)
        self.root.right = lca.Node(-3)
        self.assertEquals(lca.findLCA(-2,-3), -1)

    #checks if node constructor works as expected
    def node_constructor(self):
        self.root = lca.Node(1)
        self.assertEquals(self.root, 1)

    #checks what happens when a node that is not part of tree is queried
    def test_non_existent(self):
	self.root = lca.Node(1)
	self.root.left = lca.Node(2)
	self.root.right = lca.Node(3)
	self.root.left.left = lca.Node(4)
	self.root.left.right = lca.Node(5)
	self.root.right.left = lca.Node(6)
	self.root.right.right = lca.Node(7)

	self.assertEquals(lca.findLCA(8, 9), -1);#-1 = FALSE
	self.assertEquals(lca.findLCA(33, 132), -1)

    #checks to see if program can find LCA with only two nodes
    def test_only_two(self):
        self.root = lca.Node(1)
        self.root.right = lca.Node(2)
        self.assertEquals(lca.findLCA(1, 2), 1)
        

    
