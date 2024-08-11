#!/usr/bin/env python3

import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    with open(markdown_file, 'r') as md_file:
        lines = md_file.readlines()
    
    html_lines = []

    for line in lines:
        line = line.rstrip('\n')  # Remove trailing newline
        if line.startswith('#'):
            # Count the number of '#' to determine heading level
            heading_level = line.count('#')
            if 1 <= heading_level <= 6:
                # Remove the '#' characters and leading spaces
                heading_text = line[heading_level:].strip()
                html_line = f"<h{heading_level}>{heading_text}</h{heading_level}>"
                html_lines.append(html_line)
            else:
                html_lines.append(line)
        else:
            # Handle non-heading lines as plain text (or additional processing can be done)
            html_lines.append(f"<p>{line}</p>")

    with open(output_file, 'w') as out_file:
        out_file.write("\n".join(html_lines) + "\n")

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(markdown_file, output_file)

    # If everything is successful, exit with code 0
    sys.exit(0)

if __name__ == "__main__":
    main()
