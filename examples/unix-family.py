#!/usr/bin/python
#
# Outputs the Unix Family 'Tree', such as shown in:
# http://www.graphviz.org/Gallery/directed/unix.html
#
import gvgen

graph = gvgen.GvGen()

graph.styleDefaultAppend("color","lightblue2")
graph.styleDefaultAppend("style","filled")

cbunix1 = graph.newItem("CB Unix 1")
cbunix2 = graph.newItem("CB Unix 2")
cbunix3 = graph.newItem("CB Unix 3")
interdata = graph.newItem("Interdata")
lsx   = graph.newItem("LSX")
miniunix = graph.newItem("Mini Unix")
n1bsd = graph.newItem("1 BSD")
n28bsd = graph.newItem("2.8 BSD")
n29bsd = graph.newItem("2.9 BSD")
n2bsd = graph.newItem("2 BSD")
n32v = graph.newItem("32V")
n3bsd = graph.newItem("3 BSD")
n41bsd = graph.newItem("4.1 BSD")
n42bsd = graph.newItem("4.2 BSD")
n43bsd = graph.newItem("4.3 BSD")
n4bsd = graph.newItem("4 BSD")
n5th  = graph.newItem("5th Edition")
n6th  = graph.newItem("6th Edition")
n7th = graph.newItem("7th Edition")
n8th = graph.newItem("8th Edition")
n9th = graph.newItem("9th Edition")
pdp11 = graph.newItem("PDP-11 Sys V")
pwb10 = graph.newItem("PWB 1.0")
pwb12 = graph.newItem("PWB 1.2")
pwb20 = graph.newItem("PWB 2.0")
sys0 = graph.newItem("System V.0")
sys2 = graph.newItem("System V.2")
sys3 = graph.newItem("System V.3")
ts40 = graph.newItem("TS 4.0")
ultrix11 = graph.newItem("Ultrix-11")
ultrix32 = graph.newItem("Ultrix-32")
uniplus = graph.newItem("UniPlus+")
unixts10 = graph.newItem("Unix/TS 1.0")
unixts30 = graph.newItem("Unix/TS 3.0")
unixtspp = graph.newItem("Unix/TS++")
usg10 = graph.newItem("USG 1.0")
usg20 = graph.newItem("USG 2.0")
usg30 = graph.newItem("USG 3.0")
v7m = graph.newItem("V7M")
wollongong = graph.newItem("Wollongong")
xenix = graph.newItem("Xenix")


graph.newLink(n5th,n6th)
graph.newLink(n5th,pwb10)

graph.newLink(pwb10,pwb12)
graph.newLink(pwb10,usg10)
graph.newLink(n6th,n1bsd)
graph.newLink(n6th,interdata)
graph.newLink(n6th,miniunix)
graph.newLink(n6th,wollongong)
graph.newLink(n6th,lsx)

graph.newLink(interdata,n7th)
graph.newLink(interdata,pwb20)
graph.newLink(pwb12,pwb20)
graph.newLink(usg10,usg20)
graph.newLink(usg10,cbunix1)

graph.newLink(n7th,xenix)
graph.newLink(n7th,uniplus)
graph.newLink(n7th,n32v)
graph.newLink(usg20,usg30)
graph.newLink(cbunix1,cbunix2)

graph.newLink(n7th,v7m)
graph.newLink(n32v,n3bsd)
graph.newLink(interdata,unixts30)
graph.newLink(usg30,unixts30) 
graph.newLink(unixts10,unixts30)
graph.newLink(cbunix2,cbunix3)

graph.newLink(n3bsd,n4bsd)
graph.newLink(cbunix3,unixtspp)
graph.newLink(cbunix3,pdp11)

graph.newLink(n1bsd,n2bsd)
graph.newLink(n4bsd,n41bsd)
graph.newLink(unixts30,ts40)
graph.newLink(cbunix3,ts40)
graph.newLink(unixtspp,ts40)

graph.newLink(n2bsd,n28bsd)
graph.newLink(n41bsd,n28bsd)
graph.newLink(n41bsd,n42bsd)
graph.newLink(n41bsd,n8th)
graph.newLink(ts40,sys0)

graph.newLink(v7m,ultrix11)
graph.newLink(n7th,ultrix11)
graph.newLink(n28bsd,ultrix11)
graph.newLink(n28bsd,n29bsd)
graph.newLink(n42bsd,ultrix32)
graph.newLink(n42bsd,n43bsd)
graph.newLink(n8th,n9th)
graph.newLink(sys0,sys2)

graph.newLink(sys2,sys3)

graph.dot()

