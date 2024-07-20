# File: write_file.py

# Open a file in write mode ('w')
with open('sample.txt', 'w') as f:
    f.write("Hello, this is a sample file.\n")
    f.write("This file is used to demonstrate file operations in Python.\n")
    f.write("Writing to a file is simple with Python!\n")

print("Data has been written to 'sample.txt'")

# File: read_file.py

# Open the file in read mode ('r')
with open('sample.txt', 'r') as f:
    # Read and print each line
    for line in f:
        print(line.strip())
