#!/bin/bash
# This script displays the body of a response
curl -I -s -X OPTIONS "$1" | grep -i "^Allow:" | sed "s/^Allow: //"
