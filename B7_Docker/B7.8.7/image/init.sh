#!/bin/bash
echo "Init" > /tmp/log
echo "Alias: $1" >> /tmp/log
echo "Script path: $2" >> /tmp/log
shopt -s expand_aliases
alias $1=$2 >> /tmp/log