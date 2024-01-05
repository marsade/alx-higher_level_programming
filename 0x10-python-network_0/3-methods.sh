#!/bin/bash
# This script displays the body of a response
curl -X -s -I OPTIONS "$1" | grep -i "^Allow:" | sed "s/^Allow: //"
