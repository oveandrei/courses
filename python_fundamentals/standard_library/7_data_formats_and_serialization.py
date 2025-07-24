'''csv'''

import csv

# Writing to a CSV file
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
    writer.writerow(['Bob', 25])

# Reading from a CSV file
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) # ['Name', 'Age'], then ['Alice', '30'] etc.

# Using DicWriter and DictReader
with open('people_dict.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': "Charlie", "Age":40})


'''sqlite3'''

import sqlite3

# Connect to a database (or create if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (it INTEGER PRIMARY KEY, name TEXT)")

# Insert a row
cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
conn.commit()

# Query the data
cursor.execute('SELECT * FROM users')
print(cursor.fetchall()) # [(1, 'Alice')]

# Close the connection
conn.close()


'''zipfile'''

import zipfile

# Create a ZIP file
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('people.csv') # Adds file to the archive

# Extract ZIP file
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extracted_files') # Extracts all contents


'''tarfile'''

import tarfile

# Create a TAR.GZ file
with tarfile.open('archive.tar.gz', 'w:gz') as tar:
    tar.add('people.csv')

# Extract TAR file
with tarfile.open('archive.tar.gz', 'r:gz') as tar:
    tar.extractall('extracted_tar')


'''zlib'''

import zlib

data = b"This is some data that needs to be compressed."

# Compress data
compressed = zlib.compress(data)
print(compressed)

# Decompress data
original = zlib.decompress(compressed)
print(original.decode()) # 'This is some data that needs to be compressed.'


'''bz2'''

import bz2

data = b"Bzip2 is another compression method."

# Compress
compressed = bz2.compress(data)
print(compressed)

# Decompress
print(bz2.decompress(compressed). decode()) # Bzip2 is another compression method.


'''lzma'''

import lzma

data = b"LZMA offers very high compression ratio."

# Compress
compressed = lzma.compress(data)

# Decompress
print(lzma.decompress(compressed).decode()) # 'LZMA offers very high compression ratio.'