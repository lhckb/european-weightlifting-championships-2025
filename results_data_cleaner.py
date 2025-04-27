import re
import sys
import os

# Base directory for the data files
BASE_DIR = "/Users/luiscruz/Desktop/ewc-2025-nasar-wr-analysis/data/"

# Function to process each line
def process_line(line):
    # Skip the header or comment lines
    if line.startswith("//") or line.startswith("Standing,"):
        return line.strip()
    
    # Use regex to split the line into columns while preserving the athlete's name
    match = re.match(
        r"(\d+)\s+([A-Z]+[a-zA-Z\s]+)\s+(\d{2}\.\d{2}\.\d{4})\s+(\w+)\s+([A-Z])\s+([\d.]+)\s+(\d+|0)\s+(\d+|0)\s+(\d+|0)",
        line.strip()
    )
    if match:
        standing = match.group(1)
        name = match.group(2).strip()
        born = match.group(3)
        nation = match.group(4)
        session = match.group(5)
        bodyweight = match.group(6)
        snatch = match.group(7)
        clean_and_jerk = match.group(8)
        total = match.group(9)
        return f"{standing},{name},{born},{nation},{session},{bodyweight},{snatch},{clean_and_jerk},{total}"
    return line.strip()

def main():
    # Ensure the script is called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python results_data_cleaner.py <file_name>")
        sys.exit(1)

    # Get the file name from the command-line arguments
    file_name = sys.argv[1]

    # Construct the full input and output file paths
    input_file = os.path.join(BASE_DIR, file_name)
    output_file = os.path.join(BASE_DIR, os.path.splitext(file_name)[0] + "_cleaned.csv")

    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # Read the input file and process each line
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            cleaned_line = process_line(line)
            outfile.write(cleaned_line + "\n")

    print(f"File processed and saved to {output_file}")

if __name__ == "__main__":
    main()