import pandas as pd

def sort_dataset(dataset_df):
	#TODO: Implement this function

def split_dataset(dataset_df):	
	#TODO: Implement this function

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function

def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))