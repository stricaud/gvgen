#!/usr/bin/python

import gvgen

# Creates the new graph instance
graph = gvgen.GvGen()

# Creates two items labeled "Foo" and "Bar"
ggggp = graph.newItem("grand grand grand grand parent")
gggp = graph.newItem("grand grand grand parent", ggggp)
ggp = graph.newItem("grand grand parent", gggp)
gp = graph.newItem("grand parent", ggp)
p = graph.newItem("parent", gp)
c1 = graph.newItem("child 1", p)
c2 = graph.newItem("child 2", p)
# Links from "foo" to "bar"
graph.newLink(c1,c2)

tof = graph.newItem("this other family")
graph.newItem("The children", tof)

# Outputs the graphviz code
graph.dot()

