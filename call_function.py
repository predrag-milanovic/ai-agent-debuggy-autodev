from google.genai import types

from functions.get_files_info import schema_get_files_info

# Available functions for LLM to call
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)