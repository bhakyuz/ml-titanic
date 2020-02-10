# from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score 
# from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve, auc, log_loss

def measure_model(model, expected, predicted):
	'''
	preprocess data 
	df is pd data frame
	'''
	model = model.__class__.__name__
	accuracy_score=accuracy_score(expected, predicted)
	precision_score = precision_score(expected, predicted) 
	recall_score = recall_score(expected, predicted)
	# log_loss=log_loss(y_test, y_pred_proba))
	# auc=auc(fpr, tpr)

	scores = {
	'model':model
	'accuracy_score':accuracy_score,
	'precision_score':precision_score,
	'recall_score':recall_score
	}

	return(scores)
