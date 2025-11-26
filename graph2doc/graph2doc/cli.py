import os
import sys
import argparse


def build_parser():
    parser=argparse.ArgumentParser(
        description="Convert ASCII Tree-like text structures into real folder layouts"
    )
    parser.add_argument(
        "-i","--input_file",
        type=str,
        help="Path to the input text file containing the tree structure.",
        default="tree.txt",
    )
    parser.add_argument(
        "-o","--output_dir",
        type=str,
        help="Path to the output directory where the folder structure will be created.",
        default=None,
    )
    return parser
    

def parse_lines(lines):
    """
    Parse lines of ASCII tree structure into (depth, name) pairs.
    Args:
        lines (list): List of strings representing lines of the tree structure.
    Returns:
        list: List of tuples (depth, name) where depth is an integer and name is a string.
    """
    parsed = []

    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip():
            continue

        depth = 0
        i = 0
        length = len(line)

        while i < length:
            ch = line[i]

            if ch in ("│", "├", "└"):
                depth += 1
                i += 1
                continue

            if ch == "─":        # part of ──
                i += 1
                continue

            if ch == " ":        # indent padding
                i += 1
                continue

            break                # hit actual filename

        cleaned = line[i:].strip()
        parsed.append((depth, cleaned))

    return parsed

def read_file(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        lines= f.readlines()
    return lines

def write_structure(parsed_lines, output_dir):
    """
    Create folder structure based on parsed lines.

    Args:
        parsed_lines (_type_): List of (depth,name) pairs
        output_dir (_type_): Output directory path (defaults to current directory)
    """
    
    stack=[]
    for depth,name in parsed_lines:
        stack=stack[:depth]
        current_path=os.path.join(output_dir,*stack,name)
        
        # Check if it's a directory or a file
        if "." in name:
            os.makedirs(os.path.dirname(current_path),exist_ok=True)
            with open(current_path,'w',encoding='utf-8') as f:
                pass
        else:
            os.makedirs(current_path,exist_ok=True)
        stack.append(name)
        
def main():
    parser=build_parser()
    args=parser.parse_args()
    
    if not os.path.isfile(args.input_file):
        print(f"Error: File '{args.input_file}' not found.")
        sys.exit(1)
    
    print("Reading txt file...")
    lines=read_file(args.input_file)
    print("Parsing structure...")
    lines=parse_lines(lines)
    print("Creating folder structure...")
    write_structure(lines,args.output_dir or os.getcwd())
    print("Folder structure created successfully.")

if __name__=="__main__":
    main()
    