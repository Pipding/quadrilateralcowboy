#!/bin/bash

set -e

LOGFILE="build.log"

if [[ "$1" == "--clean" ]]; then
    echo "Cleaning build..." | tee "$LOGFILE"
    scons -c | tee -a "$LOGFILE"
    echo "Building..." | tee -a "$LOGFILE"
    scons | tee -a "$LOGFILE"
else
    echo "Building..." | tee "$LOGFILE"
    scons | tee -a "$LOGFILE"
fi

echo "Build complete. Run qc.bin.x86_64" | tee -a "$LOGFILE"
