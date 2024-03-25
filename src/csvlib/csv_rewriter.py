import pandas as pd
from fuzzywuzzy import fuzz

class CSVRewriter:
    def __init__(self, input_filename, output_filename, valid_columns, match_ratio=90):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.valid_columns = [x.lower() for x in valid_columns.split("|")]
        self.match_ratio = match_ratio
        try:
            self.df = pd.read_csv(input_filename, header=None)
        except Exception as e:
            raise(e)


    def match_columns(self):
        valid_columns = ",".join(self.valid_columns)
        match_ratio = self.match_ratio
        header_index, d = None, {}
        matched = False

        all_rows = [{"index":i, "value":x.tolist()} for i, x in self.df.iterrows()]
        for element in all_rows:
            index = element.get("index")
            value_str = ",".join([str(x).lower() for x in element.get("value")])
            d[index] = fuzz.ratio(value_str, valid_columns)
        d_sorted_desc = sorted(d.items(), key=lambda item:item[1], reverse = True)
        best_match = d_sorted_desc[0]
        if(best_match[1] > match_ratio):
            header_index = best_match[0]
        if header_index:
            matched = True
            self.df.drop(header_index, axis='index', inplace=True)
        return matched


    def rename_columns(self):
        valid_names = {}
        for index, column in enumerate(self.valid_columns):
            valid_names[index] = column
        self.df.rename(valid_names, axis="columns", inplace=True)


    def drop_rows(self, rows_to_drop=[]):
        self.df.drop(rows_to_drop, axis="rows", inplace=True)


    def to_csv(self):
        self.df.to_csv(self.output_filename, index=False)
