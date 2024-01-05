#!/bin/bash
# Get length of body of a request
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
