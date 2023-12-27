import os
import sys


def print_directory_structure(startpath, indent=0):
    for root, dirs, files in os.walk(startpath, topdown=True):
        # Limit the subdirectories to explore next
        # Optionally exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.startswith('.'):  # Optionally exclude hidden files
                print('{}{}'.format(subindent, f))


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please provide a file path.")
        return
    file_path = args[0]
    print_directory_structure(file_path)


if __name__ == "__main__":
    main()
