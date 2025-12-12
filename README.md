# Log Analysis Tool

A beginner-friendly Python script that analyzes log files to detect repeated login failures and identify potential brute-force attack patterns.

## Features
- Detects lines with failed login attempts
- Extracts IP addresses from logs
- Counts number of failed attempts per IP
- Flags suspicious IPs with high failure counts
- Generates a clean terminal report

## Usage

1. Clone the repository:
git clone https://github.com/DarshanMB/log-analysis-tool.git

3. Run the script:
## Example Output
=== Login Failure Analysis Report ===

Total Failed Attempts: 6

Attempts by IP:
192.168.1.100: 3 attempts
103.44.21.9: 2 attempts
185.100.87.10: 1 attempts

Suspicious IPs (more than 3 failed attempts):
192.168.1.100

## Purpose
This project helps beginners understand:
- Log file structure  
- Pattern detection  
- Basic security monitoring concepts  
- How brute-force attempts appear in logs
