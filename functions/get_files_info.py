import os
from google.genai import types
from functions.path_validator import validate_path


def get_files_info(working_directory, directory="."):   # Returns formatted directory contents with metadata as a string.
    abs_working_dir, result = validate_path(working_directory, directory)
    if abs_working_dir is None:
        return result  # Return error message
    target_dir = result
    if not os.path.isdir(target_dir):   # Validate target is actually a directory
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        # Use os.scandir for better performance
        with os.scandir(target_dir) as entries:
            for entry in entries:
                is_dir = entry.is_dir()
                file_size = 0 if is_dir else entry.stat().st_size
                files_info.append(
                    f"- {entry.name}: file_size={file_size} bytes, is_dir={is_dir}"
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