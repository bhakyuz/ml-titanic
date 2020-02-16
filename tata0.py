# following logic in
# https://www.kaggle.com/mnassrib/titanic-logistic-regression-with-python
import pandas as pd
import json
from ml.missings import get_missing_replacements

training = pd.read_csv("data-raw/train.csv")
replacements = get_missing_replacements(training)

with open('data/replacements.json', 'w') as f:
    json.dump(replacements, f)