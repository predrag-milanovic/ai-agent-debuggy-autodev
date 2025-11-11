import os
from google.genai import types
from config import MAX_CHARS    # Configurable safety limit (10000 chars)
from functions.path_validator import validate_path


def get_file_content(working_directory, file_path):
    # Convert paths to absolute form and validate containment
    abs_working_dir, result = validate_path(working_directory, file_path)
    if abs_working_dir is None:
        return result  # Return error message
    abs_file_path = result
    # Validate target exists and is a file (not dir/symlink/etc)
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        # Check file size before reading
        file_size = os.path.getsize(abs_file_path)
        # Read file with size limit
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            # Add truncation notice if file was larger than limit
            if file_size > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        # Catch filesystem/read errors and return as string
        return f'Error reading file "{file_path}": {e}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)