import re

# Input file path
input_file = "input.txt"

# Regular expression pattern
pattern = r"(/cady/sftp/cady/[^/\s]+)"

# Set to store unique paths
output = set()

# Open input file
with open(input_file, "r") as file:
    # Read file contents
    content = file.read()
    
    # Find all matches of the pattern
    matches = re.findall(pattern, content)
    
    # Add matched paths to the set
    for match in matches:
        output.add(match)

# Sort the unique paths alphabetically
sorted_paths = sorted(output)

# Output file path
output_file = "output.txt"

# Write the sorted paths to the output file
with open(output_file, "w") as file:
    file.write("\n".join(sorted_paths))

