#!/bin/bash
# This script displays the status code of the response
curl -s -o -I -w "%{http_code}" "$1"
