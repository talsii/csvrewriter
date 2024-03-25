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
python3 src/main.py \
   --input-csv-file=data/input.csv \
   --output-csv-file=data/output.csv \ 
   --match-ratio=70 \
   --valid-columns="row|Alligator|Bear|Cat|Dog|Elephant|Frog|Giraffe|Horse|Iguana|Jaguar|Kangaroo"
```


## AWS deployment

To deploy the module to an AWS account we need to build 3 resources

- Lambda layer
- Lambda role
- Lambda function

### Lambda layer
To create the lambda layer you can run these commands locally:

```sh
mkdir -p layer/python && cd layer
python3 -m venv venv
source venv/bin/activate
cd python
pip install pandas --target .
pip install python-Levenshtein --target .
pip install fuzzywuzzy --target .
rm -fr *dist-info && cd ..
zip -r lambda-layer.zip python/
aws s3 cp lambda-layer.zip s3:://<your-bucket-name>/<your-key-name>/
```

### Lambda role
To create the lambda role you can run these commands locally or using a cloudshell

```sh
aws iam create-role \
   --role-name csvrewriter-role-eu-west-1-dev
   -- assume-role-policy-document file://iam/trust-policy.json
```

Then you can attach the required policies to your lambda role




