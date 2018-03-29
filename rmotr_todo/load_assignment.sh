#!/bin/bash

ASSIGNMENT=$1

if [ "$ASSIGNMENT" != "" ]; then
	rm -rf todo
	cp -ar "solutions/$ASSIGNMENT/todo/" ./
	cp -ar "solutions/$ASSIGNMENT/rmotr_todo/" ./
fi