# python file detection
import os

file_path ="example.pdf"

if os.path.exists(file_path):
    print(f"the location of '{file_path}' exist")
else:
    print(f"location does not exist")

    