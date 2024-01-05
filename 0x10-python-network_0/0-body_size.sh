#!/usr/bin/env bash
# Get length of body of a request

if [ $# -ge 1 ]; then
  curl -sI "$1" | grep -i "Content-Length:" | awk '{print $2}'
fi
