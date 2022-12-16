#!/bin/bash

# Set a counter to track the number of times the Python script has exited
counter=0

# Set a flag to track whether the Python script has exited more than once within a minute
flag=false

# Set the timeout to one minute (60 seconds)
timeout=60
restart=5

# Start a loop to run the Python script
while true; do
  # Run the Python script using the `timeout` command
  # If the Python script takes longer than $timeout seconds to run, it will be killed
  timeout $timeout python pc_start.py

  # Increment the counter
  counter=$((counter+1))

  # If the Python script has exited more than once within a minute, set the flag to true
  if [ $counter -gt 1 ]; then
    flag=true
    break
  fi

  # Sleep for one minute before running the Python script again
  sleep $restart
done

# If the flag is true, exit the Bash script
if [ "$flag" = true ]; then
  exit
fi
