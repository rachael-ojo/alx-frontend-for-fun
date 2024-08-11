#!/usr/bin/python3

"""
markdown2html.py

A script to convert Markdown headings and unordered lists to HTML.

Usage:
    ./markdown2html.py <input_markdown_file> <output_html_file>

Arguments:
    <input_markdown_file>    Path to the Markdown file to convert.
    <output_html_file>       Path where the HTML output will be saved.

This script handles:
    - Headings (# to ######) converted to <h1> to <h6> tags.
    - Unordered lists starting with '- ' converted to <ul> and <li> tags.
    - Plain text wrapped in <p> tags.
"""

import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML, handling headings and unordered lists.

    Args:
        markdown_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.
    """
    with open(markdown_file, 'r') as md_file:
        lines = md_file.readlines()

    html_lines = []
    in_list = False

    for line in lines:
        line = line.rstrip('\n')  # Remove trailing newline

        if line.startswith('#'):
            # Handle headings
            heading_level = line.count('#')
            if 1 <= heading_level <= 6:
                heading_text = line[heading_level:].strip()  # Remove '#' and trim spaces
                html_line = f"<h{heading_level}>{heading_text}</h{heading_level}>"
                html_lines.append(html_line)
        elif line.startswith('- '):
            # Handle unordered lists
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            list_item = line[2:].strip()  # Remove '- ' and trim spaces
            html_lines.append(f"<li>{list_item}</li>")
        else:
            # End of a list or non-list lines
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            if line.strip():  # Only wrap non-empty lines in <p> tags
                html_lines.append(f"<p>{line}</p>")

    # Close any remaining open list tags
    if in_list:
        html_lines.append("</ul>")

    with open(output_file, 'w') as out_file:
        out_file.write("\n".join(html_lines) + "\n")


def main():
    """
    Main function to handle command-line arguments and initiate the conversion.
    """
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
