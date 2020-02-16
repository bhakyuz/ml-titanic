import pandas as pd
import json
from ml.preprocess import prepare_data

training = pd.read_csv("data-raw/train.csv")
with open('data/replacements.json') as f:
  replacements = json.load(f)

t = prepare_data(training, replacements)
