import os
import hashlib

class DuplicateFileRemover:
    def __init__(self, directory):
        self.directory = directory
        self.files_hashes = {}
        self.duplicates = []

    def hash_file(self, file_path, block_size=65536):
        """Generate a hash for a file."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            buf = f.read(block_size)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(block_size)
        return hasher.hexdigest()

    def find_duplicate_files(self):
        """Find duplicate files in the specified directory."""
        for dirpath, _, filenames in os.walk(self.directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_hash = self.hash_file(file_path)

                if file_hash in self.files_hashes:
                    self.duplicates.append(file_path)
                else:
                    self.files_hashes[file_hash] = file_path

    def show_duplicates(self):
        """Display the list of duplicate files."""
        if self.duplicates:
            print(f"Found {len(self.duplicates)} duplicate files:")
            for file in self.duplicates:
                print(file)
        else:
            print("No duplicate files found.")

    def delete_files(self):
        """Delete files from the duplicates list."""
        for file_path in self.duplicates:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    def execute(self):
        """Execute the duplicate file removal process."""
        self.find_duplicate_files()
        self.show_duplicates()
        
        if self.duplicates:
            confirm = input("Do you want to delete these files? (yes/no): ")
            if confirm.lower() == "yes":
                self.delete_files()
            else:
                print("No files were deleted.")

if __name__ == "__main__":
    directory_to_check = input("Enter the directory to check for duplicates: ")
    remover = DuplicateFileRemover(directory_to_check)
    remover.execute()
