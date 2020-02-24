import pandas as pd
import json
import numpy
# https://mg.readthedocs.io/importing-local-python-modules-from-jupyter-notebooks/sys-path-in-notebook/path-notebook.html
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from ml import get_missing_replacements

training = pd.read_csv("data-raw/train.csv")
replacements = get_missing_replacements(training)

# https://stackoverflow.com/questions/11942364/typeerror-integer-is-not-json-serializable-when-serializing-json-in-python
def convert(o):
	if isinstance(o, numpy.int64): return int(o)  
	raise TypeError

with open('data/replacements.json', 'w') as f:
	json.dump(replacements, f, default=convert)