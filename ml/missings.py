def get_missing_replacements(df):
	'''
	create a dict of replacement for missing values
	df is pd data frame
	'''
	# ideally same names should be used here 
	Age = df["Age"].median(skipna=True)
	Embarked = df['Embarked'].value_counts().idxmax()

	return({'Age':Age, 'Embarked':Embarked})
