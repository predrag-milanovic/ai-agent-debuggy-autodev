import os
from google.genai import types


def get_files_info(working_directory, directory="."):   # Returns formatted directory contents with metadata as a string.
    abs_working_dir = os.path.abspath(working_directory)                          # Convert paths to
    target_dir = os.path.abspath(os.path.join(working_directory, directory))      # absolute form for security checks
    if not target_dir.startswith(abs_working_dir):                                                      # Security: Prevent directory
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'     # traversal outside working directory
    if not os.path.isdir(target_dir):   # Validate target is actually a directory
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        # List all entries in the target directory
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)    # Get file metadata
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"  # Catch all filesystem errors and return as string


# Function schema for LLM to understand get_files_info capabilities
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)