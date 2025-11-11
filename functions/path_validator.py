import os


def validate_path(working_directory, file_path):
    """Validates that file_path is within working_directory.
    
    Args:
        working_directory: The base working directory
        file_path: The relative file path to validate
    
    Returns:
        tuple: (abs_working_dir, abs_file_path) if valid, or (None, error_message) if invalid
    """
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    
    if not abs_file_path.startswith(abs_working_dir):
        return None, f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
    
    return abs_working_dir, abs_file_path
