#!/usr/bin/env python3

import os
import re
from pathlib import Path

SOURCE_ROOT = './script/Nobaros Cafe'
SOURCE_EXT = ".md"
TARGET_ROOT = "./game/scripts"
TARGET_EXT = ".rpy"

def should_ignore_file(file: str) -> bool:
    return file.lower().endswith("master.md")

IGNORE_DIRS = [
    "./script/Nobaros Cafe/.obsidian"
]

def main():
    for subdir, dirs, files in os.walk(SOURCE_ROOT):
        if subdir in IGNORE_DIRS:
            print(f"igoring directory: {subdir}")
            continue
        
        for file in files:
            path = os.path.join(subdir, file)
            if should_ignore_file(path):
                print(f"igoring file: {path}")
                continue

            if file.endswith(SOURCE_EXT):
                write(path)


def write(source_path: str) -> None:
    suffix = source_path[len(SOURCE_ROOT):]
    target_path = f"{TARGET_ROOT}{suffix}".replace(" ", "_").lower()
    target_path = target_path.removesuffix(SOURCE_EXT) + TARGET_EXT
    file_name_idx = target_path.rfind("/")
    directory_path = target_path[:file_name_idx]

    Path(directory_path).mkdir(parents=True, exist_ok=True)
    
    with open(source_path, "r") as fr:
        lines = [line for l in fr.readlines() if (line := l.strip())]

    if len(lines) > 0 and not lines[0].startswith("#"):
        lines.insert(0, f"# {target_path[file_name_idx+1:]}".removesuffix(TARGET_EXT))

    validate(lines)
    
    if not Path(target_path).is_file() or os.stat(target_path).st_size == 0:
        print(f"generating {source_path} ==> {target_path}")
        generate_new(target_path, lines)
        return
    
    with open(target_path) as fe:
        existing_lines: list[str] = fe.readlines()

    dialog_indices: list[int] = []
    for (i, line) in enumerate(existing_lines):
        if re.match(r".+ \"*\"", line):
            dialog_indices.append(i)

    source_lines = [l for l in lines if not l.startswith("#")]
    if len(dialog_indices) != len(source_lines):
        print(f"ERROR - {target_path[len(TARGET_ROOT):]} and {source_path[len(SOURCE_ROOT):]} have different number of lines: rpy = {len(dialog_indices)}, md = {len(source_lines)}")
        return
    
    print(f"modifying {source_path} ==> {target_path}")
    for (i, l) in enumerate(source_lines):
        current: str = existing_lines[dialog_indices[i]]
        num_leading_spaces = len(current) - len(current.lstrip())
        existing_lines[dialog_indices[i]] = f"{' '*num_leading_spaces}{convert_line(l)}"
    
    with open(target_path, "w") as fw:
        fw.writelines(existing_lines)
        

def validate(source_lines: list[str]) -> None:
    for (i, l) in enumerate(source_lines):
        # new label
        if l.startswith("#"):
            continue
        # narrator
        elif l.startswith("*"):
            assert l.endswith("*"), f"narrator line {i+1} '{l}' does not end with '*'"
        else: # character, convert name to lowercase
            assert re.match(r".+ \"*\"", l), f"dialogue line {i+1} '{l}' is invalid"


def convert_line(line: str) -> str:
    # narrator
    if line.startswith("*"):
        result = line.removeprefix("*").removesuffix("*")
        return f"narrator \"{result}\"\n"
    
    # character, convert name to lowercase
    char = line.split(":")[0].lower()
    result = f"{char}{line[len(char)+1:]}"
    return f"{result}\n"


def generate_new(target_path: str, source_lines: list[str]):
    first = True
    with open(target_path, "w") as fw:
        for l in source_lines:
            # new label
            if l.startswith("#"):
                if not first:
                    fw.writelines(f"    return\n\n")
                title = l.removeprefix("#").strip().lower().replace(" ", "_")
                fw.writelines(f"label {title}:\n")
                first = False
            else:
                fw.writelines(f"    {convert_line(l)}")
        fw.writelines(f"    return\n")


if __name__ == "__main__":
    main()
