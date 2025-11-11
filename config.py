import os

MAX_CHARS = 10000
WORKING_DIR = os.getenv("AI_WORKING_DIR", "./calculator")
MAX_ITERS = int(os.getenv("AI_MAX_ITERS", "20"))