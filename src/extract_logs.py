import sys
import os

def extract_logs(log_file, target_date, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    with open(log_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            if line.startswith(target_date):
                outfile.write(line)

    print(f"Logs for {target_date} saved in {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file_path> <YYYY-MM-DD>")
        sys.exit(1)

    log_file = sys.argv[1]
    target_date = sys.argv[2]
    extract_logs(log_file, target_date)
