def get_missing_replacements(df):
	'''
	create a dict of replacement for missing values
	df is pd data frame
	'''
	# ideally same names should be used here 
	age = df["Age"].median(skipna=True)
	embarked = df['Embarked'].value_counts().idxmax()

	return({'age':age, 'embarked':embarked})
