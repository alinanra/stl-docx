import re
import os
from docx import Document

def clean_all_stl_files_in_folder(folder_path, output_filename):
    # Define the regex patterns
    timestamp_pattern = r'^\d{2}:\d{2}:\d{2}:\d{2},\d{2}:\d{2}:\d{2}:\d{2},\s*'  # Matches timestamps
    comment_pattern = r'^//.*'  # Matches lines that start with //

    # Create a new Word Document
    document = Document()

    # Loop through all .stl files in the specified folder
    for idx, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith('.stl'):
            input_filepath = os.path.join(folder_path, filename)

            # Add the name of the input file at the beginning of each section in the document
            document.add_paragraph(f"Subtitle File: {filename}\n")

            # Read the STL subtitle file
            with open(input_filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Process each line of the STL file
            for line in lines:
                # Skip lines that are comments (start with "//")
                if re.match(comment_pattern, line):
                    continue

                # Remove timestamp if present and clean up formatting
                cleaned_line = re.sub(timestamp_pattern, '', line)
                cleaned_line = cleaned_line.replace('|', ' ').strip()
                if cleaned_line:  # Only add non-empty lines
                    document.add_paragraph(cleaned_line)

            # Insert a page break after each file, except the last one
            if idx < len(os.listdir(folder_path)) - 1:
                document.add_page_break()

    # Save the cleaned-up text into a single Word file
    document.save(output_filename)
    print(f"All cleaned subtitles saved to '{output_filename}'")

# Specify the folder path containing the .stl files and output .docx file
folder_path = r"C:\Users\Chris\OneDrive\Projetos\Programming\stl clean"  # Replace with your folder path containing the .stl files
output_word_file = r"C:\Users\Chris\OneDrive\Projetos\Programming\stl clean\cleaned_subtitles.docx"  # Replace with your desired output file path

# Run the cleanup function
clean_all_stl_files_in_folder(folder_path, output_word_file)
