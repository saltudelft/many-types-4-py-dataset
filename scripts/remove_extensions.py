from argparse import ArgumentParser
import os
import pathlib

if __name__ == "__main__":
    arg_parser = ArgumentParser(description="File extension removal")
    arg_parser.add_argument('dataset', type=str, help='Dataset directory')
    arg_parser.add_argument('extension_list', type=str, help='Path of duplicate files list')
    args = arg_parser.parse_args()

    DATASET = args.dataset
    EXTENSION_LIST = args.extension_list

    extension_list_file = open(EXTENSION_LIST, 'r')
    extensions = set([ext.strip("\n") for ext in extension_list_file])
    extension_list_file.close()

    deleted_files = 0
    free_space = 0
    total_space = 0

    for root, dirs, files in os.walk(DATASET):
        for f in files:
            full_path = os.path.join(root, f)

            try:
                space = os.path.getsize(full_path)
                total_space += space

                if (os.path.splitext(full_path)[1] in extensions):
                    os.remove(full_path)
                    free_space += space
                    deleted_files += 1
            except Exception as e:
                print(e)
                
    print("Deleted files:", deleted_files)
    print("Freed space:", free_space)
    print("Space (before):", total_space)
    print("Space (after):", total_space - free_space)
