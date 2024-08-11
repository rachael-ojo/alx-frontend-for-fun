#!/usr/bin/python3

"""
markdown2html.py

A script to convert Markdown headings, unordered lists, ordered lists, and paragraphs to HTML.

Usage:
    ./markdown2html.py <input_markdown_file> <output_html_file>

Arguments:
    <input_markdown_file>    Path to the Markdown file to convert.
    <output_html_file>       Path where the HTML output will be saved.

This script handles:
    - Headings (# to ######) converted to <h1> to <h6> tags.
    - Unordered lists starting with '- ' converted to <ul> and <li> tags.
    - Ordered lists starting with '* ' converted to <ol> and <li> tags.
    - Paragraphs, with multiple lines separated by newlines and line breaks, wrapped in <p> tags.
"""

import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML, handling headings, unordered lists, ordered lists, and paragraphs.

    Args:
        markdown_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.
    """
    with open(markdown_file, 'r') as md_file:
        lines = md_file.readlines()

    html_lines = []
    in_list = False
    list_type = None
    paragraph_lines = []

    def close_current_list():
        """Close any open list tags if needed."""
        nonlocal in_list, list_type
        if in_list:
            if list_type == 'ul':
                html_lines.append("</ul>")
            elif list_type == 'ol':
                html_lines.append("</ol>")
            in_list = False
            list_type = None

    def flush_paragraph():
        """Flush the current paragraph lines to HTML."""
        nonlocal paragraph_lines
        if paragraph_lines:
            html_lines.append("<p>")
            html_lines.append("<br />\n".join(paragraph_lines).strip())
            html_lines.append("</p>")
            paragraph_lines = []

    for line in lines:
        line = line.rstrip('\n')  # Remove trailing newline

        if line.startswith('#'):
            # Handle headings
            flush_paragraph()
            heading_level = line.count('#')
            if 1 <= heading_level <= 6:
                heading_text = line[heading_level:].strip()  # Remove '#' and trim spaces
                html_line = f"<h{heading_level}>{heading_text}</h{heading_level}>"
                html_lines.append(html_line)
        elif line.startswith('- '):
            # Handle unordered lists
            flush_paragraph()
            if not in_list or list_type != 'ul':
                if in_list:
                    close_current_list()
                html_lines.append("<ul>")
                in_list = True
                list_type = 'ul'
            list_item = line[2:].strip()  # Remove '- ' and trim spaces
            html_lines.append(f"<li>{list_item}</li>")
        elif line.startswith('* '):
            # Handle ordered lists
            flush_paragraph()
            if not in_list or list_type != 'ol':
                if in_list:
                    close_current_list()
                html_lines.append("<ol>")
                in_list = True
                list_type = 'ol'
            list_item = line[2:].strip()  # Remove '* ' and trim spaces
            html_lines.append(f"<li>{list_item}</li>")
        elif line.strip():  # Non-empty line
            # Collect lines for paragraphs
            paragraph_lines.append(line)
        else:
            # Empty line indicates the end of a paragraph
            flush_paragraph()

    # Close any remaining open list tags and flush the last paragraph
    close_current_list()
    flush_paragraph()

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
