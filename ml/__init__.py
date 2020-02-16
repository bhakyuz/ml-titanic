from .missings import * 
from .measure_model import * 
from .predict import * 
from .preprocess import * 
from .train_model import * 
import json
import pickle


with open('data-raw/target_variable.json') as f:
  TARGET_VARIABLE = json.load(f)

# with open('data/replacements.json') as f:
# 	REPLACEMENTS = json.load(f)

SELECTED_FEATURES = ['Age', 'TravelAlone', 'Pclass_1', 'Pclass_2', 'Embarked_C', 'Embarked_S', 'Sex_male', 'IsMinor']

# 	unpickler = pickle.Unpickler(f);

with open('data/model.pickle', 'rb') as fp:
	MODEL = pickle.load(fp)