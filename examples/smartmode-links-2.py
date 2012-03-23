#!/usr/bin/python

import gvgen

# Creates the new graph instance
graph = gvgen.GvGen()

# We activate the smart mode
graph.smart_mode = 1
graph.max_line_width = 2
graph.max_arrow_width = 1

# Creates two items labeled "Foo" and "Bar"
a = graph.newItem("foo")
b = graph.newItem("bar")

graph.newLink(b,a)
graph.newLink(b,a)
graph.newLink(b,a)

# Outputs the graphviz code
graph.dot()

