# AI Code Assistant

A CLI tool that uses Gemini AI to debug and fix Python code. It scans files, modifies code, and tests fixes autonomously.

## Features

- Accepts coding tasks via CLI
- Uses Gemini API to reason and act
- Can:
  - Scan project files
  - Read/write code
  - Run Python scripts
- Repeats actions until task is done or fails

## Requirements

To use this project, you'll need:

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## Setup

- Create new Project and set up virtual environment:
```bash
uv init your-project-name
cd your-project-name
uv venv
echo ".venv" >> .gitignore
source .venv/bin/activate
```
- Configure API key:
```bash
echo 'GEMINI_API_KEY="your_key_here"' > .env
echo '.env' >> .gitignore
```
