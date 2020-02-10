# from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score 
# from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve, auc, log_loss

def measure_model(model, expected, predicted):
	'''
	preprocess data 
	df is pd data frame
	'''
	model = model.__class__.__name__
	n = len(expected)
	accuracy=accuracy_score(expected, predicted)
	precision = precision_score(expected, predicted) 
	recall = recall_score(expected, predicted)
	# log_loss=log_loss(y_test, y_pred_proba))
	# auc=auc(fpr, tpr)

	scores = {
	'model':model,
	'n':n,
	'accuracy_score':accuracy,
	'precision_score':precision,
	'recall_score':recall,
	}

	return(scores)
