import argparse


parser = argparse.ArgumentParser(prog="gendiff", description="Compares two configuration files and shows a difference.")


parser.add_argument("first_file")
parser.add_argument("second_file")


def main():
    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == "__main__":
    main()

"""
gendiff -h
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  """
