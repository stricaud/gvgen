#!/usr/bin/python
#
# Example of complex
# Graph representing a network
#
import gvgen

# Creates the new graph instance
graph = gvgen.GvGen(None, "overlap=\"scale\";\nlabelfloat=\"true\";\nsplines=\"true\";")

# We define different styles
graph.styleAppend("router", "shapefile", "router.png")
graph.styleAppend("router", "color", "white")
graph.styleAppend("router", "label", "")

# Creates items
insidenet = graph.newItem("Inside network")
internet = graph.newItem("Internet")

win1 = graph.newItem("Windows", insidenet)
win2 = graph.newItem("Windows", insidenet)
linux = graph.newItem("Linux", insidenet)
hurd = graph.newItem("GNU/Hurd", insidenet)
sun = graph.newItem("Sun", internet)
router = graph.newItem("Router")

# Time to apply styles and set some properties
graph.styleApply("router", router)
graph.propertyAppend(win1, "shapefile", "wingdows.png")
graph.propertyAppend(win2, "shapefile", "wingdows.png")
graph.propertyAppend(linux, "shapefile", "linux.png")
graph.propertyAppend(hurd, "shapefile", "hurd.png")
graph.propertyAppend(sun, "shapefile", "sun.png")
graph.propertyAppend(win1, "label", "")
graph.propertyAppend(win2, "label", "")
graph.propertyAppend(linux, "label", "")
graph.propertyAppend(hurd, "label", "")
graph.propertyAppend(sun, "label", "")


# Links from "foo" to "bar"
graph.newLink(win1, router)
graph.newLink(win2, router)
graph.newLink(linux, router)
graph.newLink(hurd, router)
graph.newLink(router, sun)


# Outputs the graphviz code
graph.dot()

