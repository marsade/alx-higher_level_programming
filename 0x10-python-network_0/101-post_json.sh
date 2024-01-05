#!/bin/bash
# This script sends a JSON POST request toa URL passed
curl -s -d "@$1" -X POST "$1"
