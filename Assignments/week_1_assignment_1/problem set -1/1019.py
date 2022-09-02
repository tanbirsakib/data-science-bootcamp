# Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

# Input
# The input file contains an integer N.

# Output
# Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example


seconds = int(input())
minutes = int(seconds/60)
print(minutes)
seconds %= 60
hours = int(minutes/60)
minutes %= 60

print(f'{hours}:{minutes}:{seconds}')