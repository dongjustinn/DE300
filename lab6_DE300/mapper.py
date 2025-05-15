#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            cleaned = word.strip(".,").lower()
            if len(cleaned) >= 4:
                print(f"{cleaned}\t1")

if __name__ == "__main__":
    main()