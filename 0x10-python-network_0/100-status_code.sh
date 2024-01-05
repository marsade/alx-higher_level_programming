#!/bin/bash
# This script displays the status code of the response
curl -s -I -w "%{http_code}" "$1"