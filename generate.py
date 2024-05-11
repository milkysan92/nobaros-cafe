#!/usr/bin/env python3

import os
import re
import argparse
from pathlib import Path

SOURCE_ROOT = Path("script", "Nobaros Cafe")
TARGET_ROOT = Path("game", "scripts")
TARGET_EXT = ".rpy"

def should_ignore_file(file: str) -> bool:
    return file.lower().endswith("master.md")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--files", help="the input file patterns", default="*.md")
    parser.add_argument("-r", "--regenerate", help="force the regeneration of the scripts", action="store_true")
    args = parser.parse_args()
    force_regenerate = args.regenerate
        
    for file in Path(SOURCE_ROOT).rglob(args.files):
        path: str = str(file)
        if should_ignore_file(path):
            print(f"ignoring file: {path}")
            continue

        write(file, force_regenerate)


def write(source_path: Path, force_regenerate: bool) -> None:
    source_suffix: Path = source_path.relative_to(SOURCE_ROOT)
    target_path: Path = Path(str(TARGET_ROOT / source_suffix).replace(" ", "_").lower()).with_suffix(TARGET_EXT)
    target_dir = target_path.parent
    target_dir.mkdir(parents=True, exist_ok=True)
    
    with open(source_path, "r") as fr:
        lines = [line for l in fr.readlines() if (line := l.strip())]

    validate(source_path, lines)
    
    if force_regenerate or not Path(target_path).is_file() or os.stat(target_path).st_size == 0:
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
        print(f"ERROR - '{target_path.relative_to(TARGET_ROOT)}' and '{source_suffix}' have different number of lines: rpy = {len(dialog_indices)}, md = {len(source_lines)}")
        return
    
    has_change = False
    for (i, l) in enumerate(source_lines):
        current: str = existing_lines[dialog_indices[i]]
        num_leading_spaces = len(current) - len(current.lstrip())
        new_line = f"{' '*num_leading_spaces}{convert_line(l)}"

        if current != new_line:
            has_change = True
            existing_lines[dialog_indices[i]] = new_line
    
    if has_change:
        print(f"modifying {source_path} ==> {target_path}")
        with open(target_path, "w") as fw:
            fw.writelines(existing_lines)
       

def validate(source_path: Path, source_lines: list[str]) -> None:
    assert source_lines[0].startswith("#"), f"missing title starting with # ({source_path})"
    for (i, l) in enumerate(source_lines):
        # new label
        if l.startswith("#"):
            continue
        # narrator
        elif l.startswith("*"):
            assert l.endswith("*"), f"narrator line {i+1} '{l}' does not end with '*' ({source_path})"
        else: # character, convert name to lowercase
            assert re.match(r".+: \"*\"", l), f"dialogue line {i+1} '{l}' is invalid ({source_path})"


def convert_line(line: str) -> str:
    # narrator
    if line.startswith("*"):
        result = line.removeprefix("*").removesuffix("*")
        return f"narrator \"{result}\"\n"
    
    # character, convert name to lowercase
    char = line.split(":")[0].lower()
    result = f"{char}{line[len(char)+1:]}"
    return f"{result}\n"


def generate_new(target_path: Path, source_lines: list[str]):
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
