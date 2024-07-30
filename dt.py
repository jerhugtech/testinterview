from datetime import datetime, timedelta

# Reading from a file using a relative path
with open(".\\input.txt", "r") as input_file:
    lines = input_file.readlines()

# Writing to a file using a relative path
with open(".\\output.txt", "w") as output_file:
    for line in lines:
        output_file.write(line)

print("Data has been read from input.txt and written to output.txt"
