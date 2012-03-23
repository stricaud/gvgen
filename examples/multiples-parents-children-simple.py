#!/usr/bin/python

import gvgen

# Initialisation
import gvgen
graph = gvgen.GvGen()

# Description des objets
proc = graph.newItem("/proc")
net = graph.newItem("/net", proc)
foo = graph.newItem("foo",net)
netfilter = graph.newItem("netfilter", net)
nflog = graph.newItem("nf_log", netfilter)


# Creation du dot
graph.dot()

