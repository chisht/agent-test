#!/usr/bin/env python3
"""Simple script that prints the current date."""

from datetime import datetime

if __name__ == "__main__":
    print(f"Today's date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
