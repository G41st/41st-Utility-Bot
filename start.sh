#!/bin/bash

restart_count=0

while true; do
  python pc_start.py

  restart_count=$((restart_count + 1))

  if [ "$restart_count" -ge 2 ] && [ $(($(date +%s) - $(date +%s -r my_file.py))) -lt 60 ]; then

    break

  else
    restart_count=0

  fi
done
