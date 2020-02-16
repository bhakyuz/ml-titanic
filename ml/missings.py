def get_missing_replacements(df):
	'''
	create a dict of replacement for missing values
	df is pd data frame
	'''
	# ideally same names should be used here 
	Age = df["Age"].median(skipna=True)
	Embarked = df['Embarked'].value_counts().idxmax()
	Pclass = df['Pclass'].value_counts().idxmax()
	PassengerId = 0
	Survived = df['Survived'].value_counts().idxmax()
	Name = ''
	Sex = df['Sex'].value_counts().idxmax()
	SibSp = df['SibSp'].value_counts().idxmax()
	Parch = df['Parch'].value_counts().idxmax()
	Ticket = df['Ticket'].value_counts().idxmax()
	Fare = df['Fare'].value_counts().idxmax()
	Cabin = df['Cabin'].value_counts().idxmax()

	return({'Age':Age, 
		'Embarked':Embarked,
		'Pclass':Pclass,
		'PassengerId':PassengerId,
		'Survived':Survived,
		'Name':Name,
		'Sex':Sex,
		'SibSp':SibSp,
		'Parch':Parch,
		'Ticket':Ticket,
		'Fare':Fare,
		'Cabin':Cabin,
		})
