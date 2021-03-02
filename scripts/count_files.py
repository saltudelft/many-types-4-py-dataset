from argparse import ArgumentParser
import os

arg_parser = ArgumentParser()
arg_parser.add_argument("target_dir", type=str, help="Directory to list files for")

args = arg_parser.parse_args()
DIR = args.target_dir

file_count = 0
py_count = 0

for root, dirs, files in os.walk(DIR):
     existent_files = [fname for fname in files if os.path.exists(os.path.join(root, fname))]
     file_count += len(existent_files)
     py_count += len([fname for fname in existent_files if fname.endswith(".py")])

print("Files found:", file_count)
print("Code files found:", py_count)
