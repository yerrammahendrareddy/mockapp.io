import sys

from . import mockapp

def main(args):
    if args[1] == "new" and len(args) == 4:
        mockapp.cmd.new_project(args[2], args[3])


if __name__ == "__main__":
    main(sys.argv)