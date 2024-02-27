#!/usr/bin/env python3
"""
Imports an Assimil lesson into Anki using the MP3 audio.
"""
import argparse
import os
import mutagen
import mutagen.mp3
import re
import csv


def parse_title(title: str) -> str | None:
    """
    >>> parse_title('T01-To moja gazeta')
    'To moja gazeta'
    >>> parse_title('S01-To moja gazeta')
    'To moja gazeta'
    >>> # Lessons sections are not parsed
    >>> parse_title('N10-Lekcja dziesiąta')
    """
    expr = re.compile(r"[TS](\d+)-(.*)")
    if m := expr.match(title):
        if int(m.group(1)) > 0:
            return m.group(2)

    return None


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mp3_directory",
        help="Directory where the MP3 files are stored. Will search recursively.",
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        type=argparse.FileType("w"),
        help="Where the CSV file will be loaded",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    writer = csv.writer(args.output)

    allfiles = []
    for dirpath, _, files in os.walk(args.mp3_directory):
        for f in files:
            if os.path.splitext(f)[1] != ".mp3":
                continue

            *_, lesson, _ = tuple(dirpath.split("/"))

            f = os.path.join(dirpath, f)
            allfiles.append((f, lesson))

    allfiles.sort(key=lambda s: os.path.split(s[0])[1])

    for f, lesson in allfiles:
        fileobj = mutagen.File(f)
        title = parse_title(str(fileobj.tags["TIT2"]))

        if title is not None:
            # Ask the user for the french translation
            translation = input(f"'{title}' in French? ")
            print(title, translation)

            tags = [lesson]
            line = [title, translation, ";".join(tags)]

            writer.writerow(line)


if __name__ == "__main__":
    main()
