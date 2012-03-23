#!/usr/bin/python

from gvgen import *

graph = GvGen()

parents = graph.newItem("Parents")
father = graph.newItem("Bob", parents)
mother = graph.newItem("Alice", parents)

children = graph.newItem("Children")
child1 = graph.newItem("Carol", children)
child2 = graph.newItem("Eve", children)
child3 = graph.newItem("Isaac", children)

graph.dot()
