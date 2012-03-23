#!/usr/bin/python

import gvgen

# Creates the new graph instance
graph = gvgen.GvGen()

# Creates two items labeled "Foo" and "Bar"
a = graph.newItem("foo")
b = graph.newItem("bar")

# Links from "foo" to "bar"
graph.newLink(a,b)

# Outputs the graphviz code
graph.dot()

