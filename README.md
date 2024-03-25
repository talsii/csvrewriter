# csvrewriter

CSV Rewriter python module

## Installation
CSVRewriter requires Python (https://www.python.org/) v3.9+ to run.

Install the dependencies and devDependencies.

```sh
python -m venv venv
source venv/bin/activate
pip install pandas
pip install python-Levenshtein
pip install fuzzywuzzy
```

## Local development

```sh
git clone https://github.com/talsii/csvrewriter.git
cd csvrewriter
python3 main.py \
   --input-csv-file=data/input.csv \
   --output-csv-file=data/output.csv \ 
   --match-ratio=70 \
   --valid-columns="row|Alligator|Bear|Cat|Dog|Elephant|Frog|Giraffe|Horse|Iguana|Jaguar|Kangaroo"
```
