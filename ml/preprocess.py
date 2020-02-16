import numpy as np
import pandas as pd

def prepare_data(df, replacements):
	'''
	preprocess data 
	df is pd data frame
	replacements as dict
	'''
	df2 = df.copy()
	for i in replacements.keys():
		if i in df.columns:
			df2[i].fillna(replacements.get(i), inplace=True)
		else:
			df2[i] = replacements.get(i)

	df2.drop('Cabin', axis=1, inplace=True)
	## Create categorical variable for traveling alone
	df2['TravelAlone']=np.where((df2["SibSp"]+df2["Parch"])>0, 0, 1)
	df2.drop('SibSp', axis=1, inplace=True)
	df2.drop('Parch', axis=1, inplace=True)

	final=pd.get_dummies(df2, columns=["Pclass","Embarked","Sex"])
	final.drop('Sex_female', axis=1, inplace=True)
	final.drop('PassengerId', axis=1, inplace=True)
	final.drop('Name', axis=1, inplace=True)
	final.drop('Ticket', axis=1, inplace=True)

	final['IsMinor']=np.where(final['Age']<=16, 1, 0)

	return(final)
