from sklearn.linear_model import LogisticRegression

def train_model(df, target_variable, selected_features):
	'''
	preprocess data 
	df is pd data frame
	'''
	# this should be investigated more in detail too
	if selected_features is None:
		selected_features = ['Age', 'TravelAlone', 'Pclass_1', 'Pclass_2', 'Embarked_C', 'Embarked_S', 'Sex_male', 'IsMinor']

	x = df[selected_features]
	# y = df['Survived']
	y = df[target_variable]
	# model with logistic regression

	model = LogisticRegression()
	model.fit(x, y)

	return(model)
