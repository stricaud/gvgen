#!/usr/bin/python

import gvgen

# Creates the new graph instance
graph = gvgen.GvGen("Legend")

# Creates two items labeled "Foo" and "Bar"
a = graph.newItem("foo")
b = graph.newItem("bar")

# Links from "foo" to "bar"
graph.newLink(a,b)

graph.styleAppend("foostyle","color","red")
graph.styleAppend("foostyle","shape","rectangle")
graph.styleApply("foostyle", a)

graph.styleAppend("barstyle","color","blue")
graph.styleAppend("barstyle","style","filled")
graph.styleApply("barstyle", b)

graph.legendAppend("foostyle", "Foo item",1)
graph.legendAppend("barstyle", "This is the bar item",1)

# Outputs the graphviz code
graph.dot()

