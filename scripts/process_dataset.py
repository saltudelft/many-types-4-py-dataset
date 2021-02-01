from argparse import ArgumentParser
import os
import pathlib
import shutil

if __name__ == "__main__":
    arg_parser = ArgumentParser(description="Python code duplicate removal from list")
    arg_parser.add_argument('dataset', type=str, help='Dataset directory')
    arg_parser.add_argument('duplicate_list', type=str, help='Path of duplicate files list')
    arg_parser.add_argument('copy_target', type=str, help='Dataset copy target', nargs='?', default='deduped_dataset')
    args = arg_parser.parse_args()

    DATASET = args.dataset
    DUPLICATE_LIST = args.duplicate_list
    COPY_TARGET = args.copy_target

    duplicate_list_file = open(DUPLICATE_LIST, 'r')
    duplicate_files = set([fname.strip("\n") for fname in duplicate_list_file])
    duplicate_list_file.close()

    copied_files = 0
    total_files = 0
    deleted_files = 0
    
    # Copy dataset
    for root, dirs, files in os.walk(DATASET):
        root_path = pathlib.Path(root)
        new_root = pathlib.Path(COPY_TARGET).joinpath(*root_path.parts[1:])

        copy_files = [(os.path.join(root, fname), os.path.join(new_root, fname)) for fname in files]
        
        total_files += len(copy_files)

        for cf in copy_files:
            if (os.path.exists(cf[1])):
                continue

            try:
                os.makedirs(os.path.dirname(cf[1]), exist_ok=True)
                shutil.copyfile(cf[0], cf[1])
                copied_files += 1
            except Exception as e:
                print("Failed to copy:", cf[0])
            
    print("Copied files to new dataset:", copied_files)
    print("Total files in original dataset:", total_files)

    # Delete duplicates
    for f in duplicate_files:
        if (not os.path.exists(f)):
            continue

        try:
            os.remove(f)
            deleted_files += 1
        except Exception as e:
            print(e)
    
    print("Deleted duplicates:", deleted_files)
