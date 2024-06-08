import sys
import argparse
from urllib.parse import urlparse


def main(args_):
    try:
        with open(args_.file, 'r', encoding="latin-1") as infile:
            lines = infile.readlines()
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # MAIN LOOP IN FILE
    uniques = set()
    for line in lines:
        line = line.strip()

        # If --remove-match
        if args_.remove_match:
            if args_.remove_match not in line:
                uniques.add(line)

        # If only --file and --output flags are present
        else:
            uniques.add(line)
    
    # Sort lines alphabetically
    if args_.sorted:
        uniques = sorted(uniques)

    try:
        with open(args_.output, 'w+') as outfile:
            for sorted_ in uniques:
                outfile.write(sorted_ + '\n')
    except Exception as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter same domains and sort them alphabetically.")
    parser.add_argument('--file', '-f', required=True, type=str, help="Path to the input file.")
    parser.add_argument('--output', '-o', required=True, type=str, help="Path to the output file.")
    parser.add_argument('--remove-match', '-rm', required=False, type=str, help="Remove the matched line")
    parser.add_argument('--sorted', '-sort', required=False, type=bool, default=True, help="Sort alphabetical (Default: True)")
    args = parser.parse_args()
    
    main(args)

