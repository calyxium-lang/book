#!/usr/bin/env python3
import os
import subprocess
import sys
import re
import shutil
import tempfile
import json

def is_md_file(f):
    return f.endswith(".md")

def get_md_files(test_dir):
    return [os.path.join(test_dir, f) for f in os.listdir(test_dir) if is_md_file(f)]

def run_test(file):
    try:
        result = subprocess.run(
            ["calyxium", "--no-run", file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)

        error_file_name =  ((os.path.basename(file)).split(".")[-0]) + ".md"
        if result.returncode == 0:
            print(f"Passed: {error_file_name}")
        else:
            print(f"Failed: {error_file_name}")
            with open(file, "r") as f:
                print("---- Start ----")
                print(f.read())
                print("----- End -----")
                f.close
            sys.exit(1)

    except FileNotFoundError:
        print(f"calyxium Interpreter not found")
        sys.exit(1)

def extract_calyxium_blocks(md_text):
    # Matches ```calyxium\n...\n```
    pattern = re.compile(
        r'```calyxium(?!,no)[^\n]*\n(.*?)\n```', re.DOTALL
    )
    return pattern.findall(md_text)

def get_code_blocks(md_file):
    with open(md_file, "r", encoding="utf-8") as f:
        code_blocks = extract_calyxium_blocks(f.read())
        f.close
    return code_blocks

def make_test_file(code_block, file_name=""):
    with tempfile.NamedTemporaryFile(mode="w",prefix=file_name, suffix=".cx", delete=False) as tmp:
        tmp.write(code_block)
        return tmp.name

def main():
    print("\n==== Starting Tests. ====")
    src_dir = "src"

    if shutil.which("calyxium") is None:
        print(f"calyxium Interpreter not found")
        sys.exit(1)

    if not os.path.isdir(src_dir):
        print(f"src directory not found: {src_dir}")
        sys.exit(1)

    test_files = get_md_files(src_dir)
    if not test_files:
        print("No .md files found.")
        return

    for file in test_files:
        file_name = os.path.basename(file)
        for code_block in get_code_blocks(file):
            test_file = make_test_file(code_block, file_name=file_name)
            run_test(test_file)
            os.remove(test_file)

    print("\n==== All Tests Passed. ====")

    sys.exit(1)

if __name__ == "__main__":
    main()
