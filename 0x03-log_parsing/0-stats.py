#!/usr/bin/env python3

import sys
import signal

# Signal handler to catch Ctrl+C
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Function to print statistics
def print_stats():
    global total_file_size
    global status_code_count

    print(f"File size: {total_file_size}")

    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")

# Initialize variables
total_file_size = 0
status_code_count = {}

# Register signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Main loop to read stdin
line_count = 0
try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) != 7:
            continue

        ip, date, request, status_code, file_size = parts[0], parts[3][1:], parts[5], parts[6], int(parts[7])
        if request != "GET /projects/260 HTTP/1.1":
            continue

        total_file_size += file_size

        status_code = int(status_code)
        if status_code in (200, 301, 400, 401, 403, 404, 405, 500):
            status_code_count[status_code] = status_code_count.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
