import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    db = open(sys.argv[1], "r")
    strs = db.readline().rstrip().split(",")
    strs.remove("name")
    db.close()

    bank = []
    db = open(sys.argv[1], "r")
    reader = csv.DictReader(db)
    for row in reader:
        bank.append(row)
    db.close()

    # Read DNA sequence file into a variable
    sample = open(sys.argv[2], "r")
    seq = sample.read()
    sample.close()

    # Find longest match of each STR in DNA sequence
    counts = {}
    for pattern in strs:
        counts[pattern] = str(longest_match(seq, pattern))

    # Check database for matching profiles
    for person in bank:
        matches = 0
        for pattern in strs:
            if person[pattern] == counts[pattern]:
                matches += 1
        if matches == len(strs):
            print(person["name"])
            sys.exit(0)
    print("No match")
    sys.exit(1)


def longest_match(sequence, pattern):

    # Initialize variables
    longest_run = 0
    pattern_length = len(pattern)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of pattern
    for i in range(sequence_length):
        count = 0

        # Check for a pattern match within sequence within a range
        # If a match, move one pattern length down; if not, move one base pair down
        # Continue moving and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * pattern_length
            end = start + pattern_length

            # If there is a match in the substring
            if sequence[start:end] == pattern:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # Return longest run found
    return longest_run


main()
