from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument("target_file", type=str, help="Path to count lines for")

args = arg_parser.parse_args()
FILE = args.target_file

num_lines = sum(1 for line in open(FILE))
print(num_lines)
