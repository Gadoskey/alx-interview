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
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_statistics(file_size, status_counts):
    """Prints the accumulated statistics."""
    print(f"File size: {file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption (Ctrl + C)"""
    print_statistics(total_file_size, status_codes_count)
    sys.exit(0)


# Register the signal handler for Ctrl + C
signal.signal(signal.SIGINT, signal_handler)


# Read input line by line from stdin
try:
    for line in sys.stdin:
        line_count += 1

        # Split the line into parts (no strict length requirement)
        parts = line.split()

        # Try to extract the status code and file size
        try:
            status_code = parts[-2]  # Second last item in the line is the status code
            file_size = int(parts[-1])  # Last item is the file size
        except (ValueError, IndexError):
            continue  # skip if status code or file size is invalid

        # Update the total file size
        total_file_size += file_size

        # Update the status code count if it's one of the expected codes
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # After every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_statistics(total_file_size, status_codes_count)

except KeyboardInterrupt:
    # This part is not needed since we handle SIGINT with the signal handler
    pass

# Print final statistics after the input ends
print_statistics(total_file_size, status_codes_count)
