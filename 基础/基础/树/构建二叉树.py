#coding:utf-8

#author:Elvis

class TreeNode(object):

def __init__(self):

self.data = '#'

self.l_child = None

self.r_child = None

class Tree(TreeNode):

#create a tree

def create_tree(self, tree):

data = raw_input('->')

if data == '#':

tree = None

else:

tree.data = data

tree.l_child = TreeNode()

self.create_tree(tree.l_child)

tree.r_child = TreeNode()

self.create_tree(tree.r_child)