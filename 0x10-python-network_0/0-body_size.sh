#!/bin/bash
# This script takes in a url and displays the size of the body of the response
curl -w "%{size_download}\n" "$1" -s | grep -oE "[0-9]+"
