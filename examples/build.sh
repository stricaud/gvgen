#!/bin/bash

function build()
{
    FILE=$1

    echo "Building $FILE..."
    python $FILE.py > $FILE.dot
    dot -Tpng $FILE.dot > $FILE.png
}

build edges-linking
build ex1
build ex2
build ex3
build ex4
build ex5
build ex6
build ex7
build legend
build legendin
build multiples-parents-children-simple
build parents
build properties-link
build smartmode-links
build smartmode-links-2
build smartmode-links-3
build unix-family
