# stl-docx
This is a simple code in python to compile all .stl files in a folder into one .docx file to speed up spellcheck of subtitle files.

1. Place all the desired .stl format subtitle files in a folder.
2. Copy the folder path to the corresponding part of the code.
3. Run.
4. You'll have a .docx file with:
   a. all the text from the .stl files
   b. all the line breaks and timestamps cleaned up
   c. the name of each file in the beginning of the text from each file
   d. line breaks following the end of the text of each file

*Line breaks are set to be delimited by \<br> and it can be modified in the following line:
cleaned_line = cleaned_line.replace('|', ' ').strip()
