#!/bin/bash

# Find the Uvicorn process and get its PID
PID=$(ps aux | grep 'uvicorn' | grep -v 'grep' | awk '{print $2}')

# Check if the PID was found
if [ -z "$PID" ]; then
  echo "Uvicorn process not found. Exiting."
  exit 1
else
  # Kill the Uvicorn process
  kill $PID

  # Wait for the process to be terminated
  wait $PID 2>/dev/null

  # Check if the process is successfully killed
  if kill -0 $PID 2>/dev/null; then
    echo "Failed to kill Uvicorn process with PID $PID."
  else
    echo "Uvicorn process with PID $PID has been killed successfully."
  fi
fi
