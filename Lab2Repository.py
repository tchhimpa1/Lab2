#!/usr/bin/env python3
import sys

def print_command_line_args():
    script_name = sys.argv[0]
    
    print("Script Name:", script_name)

    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
        print("Script and Variables:", script_name, *arguments)
    else:
        print("No additional variables provided.")

print_command_line_args()
