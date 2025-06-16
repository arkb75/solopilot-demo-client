#!/usr/bin/env python3
"""
A simple Hello World CLI tool.
Generated with real-time linting feedback using Claude 4 Sonnet.
"""

import sys
from typing import Optional, List


def hello_world() -> str:
    """
    Returns a Hello World greeting.
    
    Returns:
        str: The Hello World message
    """
    return "Hello, World!"


def main(args: Optional[List[str]] = None) -> int:
    """
    Main CLI entry point.
    
    Args:
        args: Command line arguments (optional)
        
    Returns:
        int: Exit code (0 for success)
    """
    try:
        if args is None:
            args = sys.argv[1:]
            
        # Simple hello world functionality
        message = hello_world()
        print(message)
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())