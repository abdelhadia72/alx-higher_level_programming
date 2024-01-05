#!/bin/bash
# Send DELETE request and display response body
curl -sLX DELETE "$1" | cat