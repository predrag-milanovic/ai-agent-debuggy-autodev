import os
from config import MAX_CHARS    # Configurable safety limit (10000 chars)


def get_file_content(working_directory, file_path):
    # Convert paths to absolute form and validate containment
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    # Security: Prevent directory traversal
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    # Validate target exists and is a file (not dir/symlink/etc)
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        # Read file with size limit
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            # Add truncation notice if file was larger than limit
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        # Catch filesystem/read errors and return as string
        return f'Error reading file "{file_path}": {e}'
