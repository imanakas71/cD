#!/bin/sh
echo $1
nkf -w8 $1|sed -f strip.sed|grep zip|sort|uniq > books.txt

