# AI Code Assistant

A CLI tool that uses Gemini AI to debug and fix Python code. It scans files, modifies code, and tests fixes autonomously.

## Features

- Accepts coding tasks via CLI
- Uses Gemini API to reason and act
- Can:
  - Scan project files
  - Read/write code
  - Run Python scripts
  - Execute tests and verify changes
- Repeats actions until task is done or fails
- Security-focused with sandboxed execution
- Optimized performance with efficient file operations

## Requirements

- Python 3.10+
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/predrag-milanovic/ai-agent-debuggy-autodev.git
cd ai-agent-debuggy-autodev
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project root:

```bash
echo 'GEMINI_API_KEY="your_key_here"' > .env
```

Replace `your_key_here` with your actual Gemini API key from [Google AI Studio](https://aistudio.google.com/).

## Configuration

The project can be configured via environment variables or by editing `config.py`:

- **`AI_WORKING_DIR`** - The working directory for code operations (default: `./calculator`)
- **`AI_MAX_ITERS`** - Maximum number of AI iterations (default: `20`)
- **`MAX_CHARS`** - Maximum characters to read from files (default: `10000`)

Example using environment variables:

```bash
export AI_WORKING_DIR="./my-project"
export AI_MAX_ITERS="30"
```

## Usage

### Basic Usage

```bash
python main.py "your prompt here"
```

### Examples

**Debug and fix code:**
```bash
python main.py "Fix the calculator to handle division by zero"
```

**Add new features:**
```bash
python main.py "Add support for square root operations"
```

**Run with verbose output:**
```bash
python main.py "Check if all tests pass" --verbose
```

### Available Functions

The AI assistant has access to the following functions:

- **`get_files_info(directory)`** - Lists files in a directory with metadata
- **`get_file_content(file_path)`** - Reads file contents (up to MAX_CHARS)
- **`write_file(file_path, content)`** - Writes content to a file
- **`run_python_file(file_path, args)`** - Executes a Python file with optional arguments

All file operations are sandboxed to the configured working directory for security.

## Quick Start

After installation, try the tool with the included calculator example:

```bash
# Test the AI assistant
python main.py "What files are in the calculator directory?"

# Ask it to analyze the code
python main.py "Explain what the calculator does"

# Ask it to run tests
python main.py "Run the calculator tests and show me the results"
```

## Testing

Run the test suite to verify everything is working:

```bash
python tests.py
```

Run the calculator's unit tests:

```bash
python calculator/tests.py
```

## Project Structure

```
ai-agent-debuggy-autodev/
├── main.py                     # Main entry point
├── config.py                   # Configuration settings
├── prompts.py                  # System prompts for AI
├── call_function.py            # Function calling logic
├── tests.py                    # Test suite
├── functions/                  # Available AI functions
│   ├── path_validator.py       # Shared path validation utility
│   ├── get_file_content.py     # Read file contents
│   ├── get_files_info.py       # List directory contents
│   ├── run_python.py           # Execute Python scripts
│   └── write_file_content.py   # Write to files
└── calculator/                 # Example project
    ├── main.py                 # Calculator CLI
    ├── tests.py                # Calculator tests
    └── pkg/
        ├── calculator.py       # Calculator logic
        └── render.py           # Output rendering
```

## How It Works

1. You provide a prompt describing what you want the AI to do
2. The AI analyzes the request and decides which functions to call
3. It can read files, analyze code, make changes, and run tests
4. The AI iterates until the task is complete or MAX_ITERS is reached
5. All operations are logged (use `--verbose` for detailed output)

The AI works autonomously within the configured working directory, making it safe to use on your projects.

## Security Features

- **Path Validation**: All file operations are restricted to the working directory
- **Sandboxed Execution**: Python scripts run with timeout and output capture
- **Input Sanitization**: File paths are validated to prevent directory traversal
- **Read Limits**: File reading is limited to prevent memory issues

## Performance Optimizations

This project includes several performance optimizations:

- **`os.scandir()`** for faster directory listing (2-3x faster than `os.listdir()`)
- **Centralized path validation** to eliminate code duplication
- **Efficient file size checks** before reading file contents
- **List comprehensions** for cleaner and faster iteration

## Troubleshooting

### API Key Issues

If you get authentication errors:
1. Verify your API key is correct in `.env`
2. Ensure the `.env` file is in the project root
3. Check that the key has API access enabled

### Python Version

If you encounter compatibility issues:
```bash
python --version  # Should be 3.10 or higher
```

### Virtual Environment

If dependencies aren't found:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Module Import Errors

If you get import errors related to `functions` module:
- Ensure you're running from the project root directory
- Check that all files in `functions/` directory exist

### Timeout Errors

If Python script execution times out (default 30 seconds):
- The script may have an infinite loop
- Consider optimizing the code being executed
- Large operations may need to be broken into smaller tasks

## Example Calculator Project

The repository includes a working calculator project in the `calculator/` directory that demonstrates:
- Basic arithmetic operations (add, subtract, multiply, divide)
- Unit tests with 9 test cases
- Proper project structure with separation of concerns
- CLI interface for user interaction

You can use this as a reference or ask the AI to modify it as a learning exercise.

## 👏 Contributing

I would love your help! Contribute by forking the repo and opening pull requests. Please ensure that your code passes the existing tests and linting, and write tests to test your changes if applicable.

All pull requests should be submitted to the `main` branch.

## License

See the [LICENSE](LICENSE) file for details.