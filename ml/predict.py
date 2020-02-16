# from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score 
# from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve, auc, log_loss

def predict(model, df, selected_features):
	'''
	preprocess data 
	df is pd data frame
	'''
	pred = model.predict(df[selected_features])
	return(pred)
