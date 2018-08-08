# Basically, file input is reading from a file and output is writing to one.
# To start, we need a file to read from and one to write to.
# input.txt is what we read from and output.txt is what we write to.

# There are a few flags that can be used when opening files for io that
# tell python what to do with the file:
# r  = read (default)
# w  = write/truncate (trunc overwrites)
# r+ = read and write
# w+ = read and write/truncate (trunc overwrites)
# a+ = read and append
# If the file does not exist, opening to write to it creates it.
# Opening with "with" makes sure the files close properly if the script crashes
infile  = open("input.txt", 'r')
outfile = open("outfile.txt", 'a+')

# Read the whole file into a variable
text = infile.read()
print(f"{text}")

# To read in a file character by character, treat it as a list
for line in text:
    # Tell the printer when the line ends
    print(f"{line}", end='')

# Alternatively, convert the file contents to listed lines with list()
lines = list(infile)
for line in lines:
    print(f"{line}")

# Writing is super easy, just write a string to the file.
outfile.write("This string will be appended because of how I opened the file handle.\n")

# Close the files manually
infile.closed
outfile.closed