#!/bin/bash
# This script takes in a url and displays the size of the body of the response
curl -w "%{size_download}\n" "$2" -s
