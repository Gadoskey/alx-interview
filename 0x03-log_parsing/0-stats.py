#!/usr/bin/python3
"""
Author: Gadoskey
File: 0-stats.py
Function: print_statistics and signal_handler
Description: A script that reads stdin line by line and computes metrics
"""

import sys
import signal

# Initialize metrics
total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_statistics():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption (Ctrl + C)"""
    print_statistics()
    sys.exit(0)


# Register the signal handler for Ctrl + C
signal.signal(signal.SIGINT, signal_handler)


# Read input line by line from stdin
try:
    for line in sys.stdin:
        line_count += 1

        # Split the line into parts
        parts = line.split()
        if len(parts) < 7:
            continue  # skip if the line doesn't have enough parts

        # Try to extract the status code and file size
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue  # skip if status code or file size is invalid

        # Update the total file size
        total_file_size += file_size

        # Update the status code count if it's one of the expected codes
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # After every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_statistics()

# Handle keyboard interrupt during reading
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
