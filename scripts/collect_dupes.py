from argparse import ArgumentParser
from dpu_utils.utils.dataloading import load_jsonl_gz
import random
import os

if __name__ == "__main__":
    arg_parser = ArgumentParser(description="Python code duplicate list creation from tokens")
    arg_parser.add_argument('token_path', type=str, help='Tokens file path', nargs='?', \
                            default='py_dataset_duplicates.jsonl.gz')
    arg_parser.add_argument('duplicate_out', type=str, help='Path to output duplicate files list', nargs='?', \
                            default='duplicate_files.txt')

    args = arg_parser.parse_args()
    TOKENS_PATH = args.token_path
    DUPLICATE_OUTPUT = args.duplicate_out

    # Selects randomly a file from each cluster of duplicate files
    clusters_rand_files = [l.pop(random.randrange(len(l))) for l in load_jsonl_gz(TOKENS_PATH)]
    duplicate_files = [f for l in load_jsonl_gz(TOKENS_PATH) for f in l]
    duplicate_files = set(duplicate_files).difference(set(clusters_rand_files))

    print(len(duplicate_files), "duplicate files present.")

    # Write file with list of duplicates
    with open(DUPLICATE_OUTPUT, "w") as dupe_file:
        dupe_file.write("\n".join(duplicate_files))
    dupe_file.write("\n")
    
    print("Written files to:", DUPLICATE_OUTPUT)
