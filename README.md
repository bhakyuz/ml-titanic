ml-titanic

Some experiental ideas on ml modeling 
some main concepts
- explore data 
-- this should be in one file that is calling function from inner things
- missing value imputation
-- first we should create with what we ll replace the values and keep them in a json/pickle so they can be reused afterward
- prepocess data
-- impute missing value
-- drop some columns
-- add some columns
-- etc,
- training
-- train model on training data
-- save the model in pickle
-- store some data points at this point so after each iteration we know what is happening
-- ideaily commit in each iteration after all the files are changed so we have a trace
- predict new data point 
-- possibly a function/rest to make the prediction both for a dataframe and a single object


even the first verison of package should give generate results
this might be even random 
meaning that from the first time we push package into PROD it will be available even if the results are not good at all

the very first version of the framework should have
- training data
- basic packages as pd, np
- the variable that we are trying to guess