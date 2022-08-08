#!/usr/bin/env python3

import os
import subprocess
import sys
import re
import html
from os.path import isfile, join
from pathlib import Path


FILES_PATH = "/usr/share/applications"
LINE_START_MATCHES = [
    "Name=",
    "Comment=",
    "Exec=",
    "Icon=",
    "Keywords=",
]


def get_entries():
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

    return entries


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
        metadata[key] = html.escape(value.strip())

    return metadata


def get_selected_entry_from_args(entries, regex=r"^<span>(?P<name>.*)<small>"):
    arguments = sys.argv[1:]
    if not arguments:
        return None

    match = re.match(regex, arguments[0])
    name = match.group("name") if match else None
    return entries[name.strip()] if name else None


def display_entry(entry):
    return "<span>{Name} <small>({Comment})</small></span>\0icon\x1f{Icon}\x1fmeta\x1f{Keywords}".format(
        **entry
    )


entries = get_entries()
selected = get_selected_entry_from_args(entries)
if selected:
    subprocess.Popen(
        selected["Exec"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    sys.exit(0)
else:
    print("\0markup-rows\x1ftrue\n")
    print("\n".join([display_entry(entry) for entry in entries.values()]))
