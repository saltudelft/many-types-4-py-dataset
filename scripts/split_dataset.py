from argparse import ArgumentParser
from sklearn.model_selection import train_test_split
import os
import pandas as pd
import sys

def list_files(directory: str) -> list:
    """
    List all .py files recursively in the given directory.
    :param directory: directory to search in
    :return: list of python code files
    """
    paths = []

    for root, dirs, files in os.walk(directory):
        paths += [os.path.join(root, fname) for fname in files if fname.endswith(".py")]

    return paths

def split_file_dataframe(df, test_ratio, valid_ratio):
    """
    Splits file dataframe into train, test, validation sets.
    Returns tuple (train_df, test_df, valid_df)

    :param: df  Dataframe to split
    :param: test_ratio  Ratio of dataframe to use for test set
    :param: valid_ratio Ratio of dataframe to use for validation set
    :return: (train_df, test_df, valid_df)
    """
    train_files, test_files = train_test_split(pd.DataFrame(df['file'].unique(), columns=['file']),
                                                test_size=test_ratio)
    train_files, valid_files = train_test_split(pd.DataFrame(df[df['file'].isin(train_files.to_numpy().flatten())]['file'].unique(),
                                                                columns=['file']), test_size=valid_ratio)

    df_train = df[df['file'].isin(train_files.to_numpy().flatten())]
    print(f"Number of files in train set: {df_train.shape[0]:,}")

    df_valid = df[df['file'].isin(valid_files.to_numpy().flatten())]
    print(f"Number of files in validation set: {df_valid.shape[0]:,}")

    df_test = df[df['file'].isin(test_files.to_numpy().flatten())]
    print(f"Number of files in test set: {df_test.shape[0]:,}")

    return df_train, df_test, df_valid

if __name__ == "__main__":
    arg_parser = ArgumentParser(description="Dataset split (train, test, validation) for dataset")
    arg_parser.add_argument('dataset', type=str, help='Dataset directory')
    arg_parser.add_argument('--od', type=str, help='CSV split output path', default='dataset_split.csv')
    arg_parser.add_argument('--test', type=float, help='Test split ratio: [0.0, 1.0)', default=0.2)
    arg_parser.add_argument('--valid', type=float, help='Validation split ratio: [0.0, 1.0)', default=0.1)

    args = arg_parser.parse_args()
    DATASET_DIR = args.dataset
    OUTPUT_PATH = args.od
    TEST_SIZE = args.test
    VALID_SIZE = args.valid

    # Create DF with all code files in target dataset
    print("Retrieving Python code files from:", DATASET_DIR)
    data_files = list_files(DATASET_DIR)
    df = pd.DataFrame(data_files, columns=['file'])

    # Split and insert corresponding type of dataset
    print("Splitting Python code files to train, test & validation sets")
    df_train, df_test, df_valid = split_file_dataframe(df, TEST_SIZE, VALID_SIZE)
    df_train.insert(0, "type", "train")
    df_test.insert(0, "type", "test")
    df_valid.insert(0, "type", "valid")

    # Write recombined output
    print("Combining train, test & validation into dataframe")
    result_df = pd.concat([df_train, df_test, df_valid])

    # https://stackoverflow.com/questions/36303919/python-3-0-open-default-encoding
    # https://stackoverflow.com/questions/1052225/convert-python-filenames-to-unicode
    print("Writing dataframe to:", OUTPUT_PATH)
    result_df.to_csv(OUTPUT_PATH, header=False, index=False, encoding=sys.getfilesystemencoding())
