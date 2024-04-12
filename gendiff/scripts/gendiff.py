import argparse


parser = argparse.ArgumentParser(prog="gendiff", description="Compares two configuration files and shows a difference.")


parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output", default="plain")


def main():
    args = parser.parse_args()
    print(args.first_file, args.second_file, args.format)


if __name__ == "__main__":
    main()
