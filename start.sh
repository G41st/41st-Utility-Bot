#!/bin/bash

counter=0

flag=false

timeout=60
restart=5

while true; do
  python3 pc_start.py

  counter=$((counter+1))

  if [ $counter -gt 1 ]; then
    flag=true
    break
  fi

  sleep $restart
done

if [ "$flag" = true ]; then
  exit
fi
