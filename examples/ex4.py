#!/usr/bin/python
import gvgen

if __name__ == "__main__":
    graph = gvgen.GvGen()
    parents = graph.newItem("Parents")
    father = graph.newItem("Bob", parents)
    mother = graph.newItem("Alice", parents)
    children = graph.newItem("Children")
    child1 = graph.newItem("Carol", children)
    child2 = graph.newItem("Eve", children)
    child3 = graph.newItem("Isaac", children)
    postman = graph.newItem("Postman")
    graph.newLink(father,child1)
    graph.newLink(father,child2)
    graph.newLink(mother,child2)
    graph.newLink(mother,child1)
    graph.newLink(mother,child3)
    graph.newLink(postman,child3)

    graph.styleAppend("Post", "color", "blue")
    graph.styleAppend("Post", "style", "filled")
    graph.styleAppend("Post", "shape", "rectangle")
    graph.styleApply("Post", postman)

    graph.dot()

