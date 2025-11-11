import os
import sys
import subprocess
from google.genai import types
from functions.path_validator import validate_path


"""Execute Python file with security constraints and return output.

Args:
    working_directory: Base directory for execution sandbox
    file_path: Relative path to Python script
    args: List of command-line arguments (optional)
    
Returns:
    str: Formatted output or error message
"""

def run_python_file(working_directory, file_path, args=None):
    # SECURITY: Resolve absolute paths and validate containment
    abs_working_dir, result = validate_path(working_directory, file_path)
    if abs_working_dir is None:
        return result  # Return error message
    abs_file_path = result
    # Validate file existence and type
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        # Prepare command with arguments - use sys.executable for current Python interpreter
        commands = [sys.executable, abs_file_path]
        if args:
            commands.extend(args)   # Add any additional arguments
        # SAFE EXECUTION: Critical security parameters
        result = subprocess.run(
            commands,
            capture_output=True,    # Prevent direct console output
            text=True,              # Get strings instead of bytes
            timeout=30,             # Prevent infinite execution
            cwd=abs_working_dir,    # Contain execution to working dir
        )
        # Format multi-part output
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)