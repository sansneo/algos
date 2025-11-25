from os import listdir
from os.path import isfile, join, basename, islink
from collections import deque
import sys

def tree(directory, depth):
    """
    Slee, slow tree(1) in Python!
    Handles symbolic links and permission errors.
    """
    try:
        entries = listdir(directory)
    except (PermissionError, FileNotFoundError, NotADirectoryError):
        print(depth + "[Error accessing directory]")
        return
    queue = deque() # To be unfolded
    for file in sorted(entries):
        path = join(directory, file)
        try:
            if islink(path):
                print(depth + file + " -> [symlink]")
            elif isfile(path):
                print(depth + file)
            else:
                queue.append(path)
        except PermissionError:
            print(depth + file + " [Permission denied]")
    for subdirectory in queue:
        print(depth + basename(subdirectory))
        tree(subdirectory, depth + "    ")
if len(sys.argv) > 1:
    depth = ""
    tree(sys.argv[1], depth)
else:
    print("Slee, the slow tree(1) implementation.\nUsage: python slee.py <path>")
