#!/bin/bash
# This script displays the body and sets a header
curl -sb -H "$1" --header "X-School-User-Id: 98"
