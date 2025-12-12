from collections import defaultdict

def analyze_log(file_path):
    failed_attempts = defaultdict(int)

    try:
        with open(file_path, "r") as file:
            for line in file:
                if "Failed password" in line:
                    parts = line.split()
                    if "from" in parts:
                        ip_index = parts.index("from") + 1
                        ip = parts[ip_index]
                        failed_attempts[ip] += 1

        print("\n=== Login Failure Analysis Report ===\n")
        total = sum(failed_attempts.values())
        print(f"Total Failed Attempts: {total}\n")

        print("Attempts by IP:")
        for ip, count in failed_attempts.items():
            print(f"  {ip}: {count} attempts")

        print("\nSuspicious IPs (more than 3 failed attempts):")
        for ip, count in failed_attempts.items():
            if count > 3:
                print(f"  {ip}: {count} attempts")

    except FileNotFoundError:
        print("Error: Log file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the analyzer
if __name__ == "__main__":
    analyze_log("sample.log")
