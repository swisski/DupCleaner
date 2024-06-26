# Duplicate File Remover
The `DuplicateFileRemover` script is a Python utility designed to identify and remove duplicate files within a specified directory. This script computes SHA-256 hashes for each file to detect duplicates, providing an option to delete them to free up space and reduce clutter.

## Features
Deep Scanning: Recursively scans the specified directory to find all duplicate files.
SHA-256 Hashing: Uses SHA-256 hashing to ensure accurate detection of duplicates.
Safe Deletion: Offers a user confirmation before deleting files to prevent accidental data loss.

## Usage
Download duplicate_file_remover.py to your local machine.
Enter the folder you wish to scan
Run $python3 duplicate_file_remover.py
Choose whether to delete the duplicates based on the confirmation prompt.
