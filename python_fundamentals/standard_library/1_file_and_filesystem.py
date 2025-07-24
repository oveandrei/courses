
'''OS module provides a way of using operating system dependent functionality like reading or writing to the file system, environment variables, etc.'''

import os

# Example 1: Listing files in the current directory
files = os.listdir('.') # Lists all files and folders in the current directory

# Example 2: Get environment variable
home = os.environ.get("Home") # Gets the HOME environment variable

# Example 3: Creating a directory
os.mkdir('new_folder') # Creates a new folder named 'new_folder'

# Example 4: Remove a file
os.remove("old_file.txt") # Deletes teh file 'old_file.txt'


'''shutil module provides a higher-level interface for file operations, such as copying, moving, and deleting files and directories.'''

import shutil

# Example 1: Copy a file
shutil.copy('source.txt', 'backup.txt') # Copies source.txt to backup.txt

# Example 2: Move a file
shutil.move('backup.txt', 'archive/backup.txt') # Moves backup.txt to archive folder

# Example 3: Deletes a directory
shutil.rmtree('old_folder') # Recursively deletes 'old_folder" and all its contents


'''glob module provides a way to find all the pathnames matching a specified pattern according to the rules used by the Unix shell.'''

import glob

# Example 1: Get all .txt files in the current directory
txt_files = glob.glob('*.txt') # Returns a list of all .txt files

# Example 2: Recursive search
all_logs = glob.glob('**/*.log', recursive=True) # Finds all .log files in all subdirectories


'''pathlib module provides an object-oriented approach to handle filesystem paths. It allows for easy manipulation of file paths and directories.'''

from pathlib import Path

# Example 1: Create a Path object and read text
path = Path('example.txt')
content = path.read_text() # Reads the content of the file

# Example 2: Write to a file
path.write_text('Hello World!') # Overwrites the file with this text

# Example 3: Check if file exists
exists = path.exists() # Returns True if file exists

# Example 4: Join paths
data_path = Path('data') / 'input.csv' # Creates a combined path object

'''tempfile module provides functions to create temporary files and directories. These files are automatically deleted when closed or when the program exists.'''

import tempfile

# Example 1: Temporary file with automatic cleanup
with tempfile.NamedTemporaryFile(delete=True) as tmp:
    tmp.write(b"Hello, temp file!")
    tmp.seek(0)
    print(tmp.read()) # Prints: b'Hello, temp file!'

# Example 2: Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Temporary directory created at: {tmpdir}")
    # Directory is deleted after the block ends.