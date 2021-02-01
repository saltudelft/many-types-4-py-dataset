import os
import csv
import pandas as pd
from argparse import ArgumentParser

def create_file_dataframe(dataset, pickle_path):
   print("Scanning dataset:", dataset)
   files_list = []
   for root, dirs, files in os.walk(dataset):
      full_paths = [os.path.join(root, fname) for fname in files]

      for f in full_paths:
         if (os.path.exists(f)):
               files_list.append([f, os.path.getsize(f)])

   df = pd.DataFrame(files_list, columns=['file', 'size'])
   df.to_pickle(pickle_path)
   print("Pickled dataframe saved to:", pickle_path)

def pretty_print_df(df):
   with pd.option_context('display.max_rows', None, 'display.max_columns', None):
      print(df)

if __name__ == "__main__":
   arg_parser = ArgumentParser(description="File structure analysis tool")
   arg_parser.add_argument('pickle_path', type=str, help='Path to output duplicate files list')
   arg_parser.add_argument('dataset', type=str, help='Path to dataset', nargs='?')
   args = arg_parser.parse_args()

   DATASET_PATH = args.dataset
   PICKLE_PATH = args.pickle_path

   if (not os.path.exists(PICKLE_PATH)):
      print("Creating file dataframe")
      create_file_dataframe(DATASET_PATH, PICKLE_PATH)

   df = pd.read_pickle(PICKLE_PATH)
   print(df)

   # Extract file extensions
   df['file'] = df['file'].apply(lambda f: os.path.splitext(f)[1])

   # Get total sizes & counts per extension
   sums = df.groupby(by="file").agg(size=('size', 'sum'), count=('file', 'count'))

   # Get sorted DF
   sorted_sums = sums.sort_values(by='size', ascending=False)
   pretty_print_df(sorted_sums)
   print("Total size:", sums['size'].sum())
