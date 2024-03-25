import argparse, sys
from csvlib import csv_rewriter

def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-csv-file", help="input csv file path")
    parser.add_argument("--output-csv-file", help="output csv file path")
    parser.add_argument("--match-ratio", help="header columns match ratio")
    parser.add_argument("--valid-columns", help="list of valid column names separated by pipes")
    return vars(parser.parse_args())

# main
args = args_parser()
input_csv_file = args.get("input_csv_file")
output_csv_file = args.get("output_csv_file")
match_ratio = int(args.get("match_ratio"))
valid_columns = args.get("valid_columns")

# init class object
csvw = csv_rewriter.CSVRewriter(input_csv_file, output_csv_file, valid_columns, match_ratio)

# match columns
matched = csvw.match_columns()
if(matched):
    csvw.rename_columns()
    rows_any_nan = csvw.df.isna().all(axis=1)
    rows_to_drop = [i for i, v in enumerate(rows_any_nan) if v]
    csvw.drop_rows(rows_to_drop)
    csvw.to_csv()
print(csvw.df)
