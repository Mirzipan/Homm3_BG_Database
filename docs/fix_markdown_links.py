import os
import re

# Path to the directory containing markdown files
directory_path = 'artifacts'  # Change this to your target directory

# Regex pattern to match `(` not followed by `..`
pattern = re.compile(r'\((?!\.\.)')

# Function to process each markdown file
def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace `(` not followed by `..` with `(../`
    modified_content = pattern.sub('(../', content)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print(f"Processed file: {file_path}")

# Iterate through all markdown files in the specified directory
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            process_markdown_file(file_path)

print("Finished processing all markdown files.")
