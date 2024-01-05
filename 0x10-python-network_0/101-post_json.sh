#!/bin/bash
# This script sends a JSON POST request toa URL passed
curl -s -d "@$2" -X POST "$1"
