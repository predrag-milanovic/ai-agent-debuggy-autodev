import os
import subprocess


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
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    # SECURITY: Prevent directory traversal attacks
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    # Validate file existence and type
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        # Prepare command with arguments
        commands = ["python", abs_file_path]
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
