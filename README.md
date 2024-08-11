Markdown to HTML Conversion Script
Overview
The markdown2html.py script is a simple utility for converting Markdown files to HTML format. It performs basic checks to ensure the correct usage and the existence of the specified Markdown file.

Usage
To use the script, run it from the command line with the following syntax:

bash
Copy code
./markdown2html.py <input_markdown_file> <output_html_file>
Arguments
<input_markdown_file>: The path to the Markdown file that you want to convert to HTML.
<output_html_file>: The path where the converted HTML file will be saved.
Example
bash
Copy code
./markdown2html.py README.md README.html
This command will check if README.md exists and if so, it will convert it to README.html.

Error Handling
The script performs the following checks:

Insufficient Arguments: If fewer than two arguments (excluding the script name) are provided, it prints a usage message to STDERR and exits with code 1.

File Not Found: If the specified Markdown file does not exist, it prints an error message indicating the missing file to STDERR and exits with code 1.

Successful Execution: If the arguments are correct and the Markdown file exists, the script exits with code 0, indicating successful completion.

Requirements
Python 3.x
Ensure that the script is executable (chmod +x markdown2html.py on Unix-like systems).
License
This script is provided as-is. Feel free to modify and use it according to your needs.
