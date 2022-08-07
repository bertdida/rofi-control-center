#!/usr/bin/env python3

import os
import subprocess
import sys
from os.path import isfile, join
from pathlib import Path


FILES_PATH = "/usr/share/applications"
LINE_START_MATCHES = [
    "Name=",
    # "Comment=",
    "Exec=",
    "Icon=",
    "Keywords=",
]


def parse_file(file_path):
    relevant_lines = []
    with open(file_path) as file_obj:
        for line in file_obj:
            if any(line.startswith(m) for m in LINE_START_MATCHES):
                relevant_lines.append(line.strip())
                continue

    metadata = {
        "FilePath": file_path,
    }

    for line in relevant_lines:
        key, value = line.split("=")
        metadata[key] = value.strip()

    return metadata


entries = {}
for desktop_file in os.listdir(FILES_PATH):
    file_path = join(FILES_PATH, desktop_file)
    if not isfile(file_path):
        continue

    base_name = Path(desktop_file).resolve().stem
    if not base_name.startswith("gnome-") or not base_name.endswith("-panel"):
        continue

    entry = parse_file(file_path)
    entries[entry["Name"]] = entry


def display_entry(entry):
    return "{} \0icon\x1f{}\x1fmeta\x1f{}".format(
        entry["Name"], entry["Icon"], entry["Keywords"]
    )


argument = sys.argv[1:]
if argument:
    selected = entries.get(argument[0].strip(), None)
    if selected:
        subprocess.Popen(
            selected["Exec"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

    sys.exit(0)
else:
    print("\n".join([display_entry(entry) for entry in entries.values()]))
