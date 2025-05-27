import json
import sys

def validate_json(input_str):
    if len(input_str) > 1000:
        raise ValueError("Input string too long")
    if not input_str.strip():
        return "Error: Empty input"
    try:
        parsed = json.loads(input_str)
        if not isinstance(parsed, dict):
            return "Error: JSON must be a dictionary"
        if "user" not in parsed:
            return "Error: Missing 'user' key"
        if not isinstance(parsed["user"], str) or len(parsed["user"]) > 50:
            return "Error: Invalid 'user' value"
        return "Valid JSON"
    except json.JSONDecodeError:
        return "Error: Invalid JSON syntax"
    except Exception as e:
        return f"Error: Unexpected error - {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            input_str = f.read()
    else:
        input_str = sys.stdin.read()
    result = validate_json(input_str)
    print(result)
