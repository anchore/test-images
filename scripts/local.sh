#!/usr/bin/env bash

# This script is only meant to run from Makefile in the parent directory of this repository

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

if [ $# -eq 0 ]
  then
    echo "No arguments supplied, this command requires an image tag to build, like:"
    for directory in  $(ls "$SCRIPTPATH/../containers"); do
	echo "- $directory"
    done
    exit 1
fi

CONTAINER=$1

cd "$SCRIPTPATH/../containers/$CONTAINER"
if [ $? != 0 ]; then
	echo "$CONTAINER is not a Makefile target or container to build. If trying to build a container locally"
	echo "then it must be one of:"
	for directory in  $(ls "$SCRIPTPATH/../containers"); do
		echo "- $directory"
	done
	echo ""
	echo "For other Makefile targets use:"
	echo "    make help"
	echo ""
	exit 2
fi

make build
