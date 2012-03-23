#!/usr/bin/python

import gvgen

# Creates the new graph instance
graph = gvgen.GvGen()

# We activate the smart mode
graph.smart_mode = 1
graph.line_factor = 3
graph.arrow_factor = 1

# Creates two items labeled "Foo" and "Bar"
a = graph.newItem("foo")
b = graph.newItem("bar")

# Links from "foo" to "bar"
graph.newLink(a,b)
graph.newLink(a,b)

# Outputs the graphviz code
graph.dot()

