#!/bin/bash
# This script displays tall the http methods the server will accept
curl -I -s -X OPTIONS "$1" | grep -i "^Allow:" | sed "s/^Allow: //"
