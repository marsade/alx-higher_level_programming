#!/bin/bash
# This script sends a POST request
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
