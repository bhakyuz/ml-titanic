## ml-titanic: from data cleaning to deploying
As it can be seen in the code, in the first version, there is no original work is included, Instead, I just followed the logistic regression implementation in this [Kaggle](https://www.kaggle.com/mnassrib/titanic-logistic-regression-with-python) Kernel provided by [Baligh Mnassri](https://www.kaggle.com/mnassrib)
Model is deployed to free hosted Heroku application which can be found [here](https://bhakyuz-ml-titanic.herokuapp.com/). The API provides the prediction for parameters that are provided in the URL query string (by default since no data is provided, missing values are imputed). Some simple examples include:
-   [Prediction for a female passenger](https://bhakyuz-ml-titanic.herokuapp.com/?Sex=female)
-   [Prediction for a male passenger](https://bhakyuz-ml-titanic.herokuapp.com/?Sex=male)

## Main steps and iterations
The following list includes required methods, steps and ideally each should be independent and coded in separate methods. The list is not sorted according to importance nor strict implementation order while I tend to follow this order. Personally, I think it is a more iterative process and requires many back and forth between the steps:
 - [ ] Documentation of all: It is done in `pmd` file that dynamically produces the [html documentation](documentation.html). 
 - [x] Reading data: This is simply done by `pandas.read_csv` in this repo, but it is likely required to have a method to read data from (from csv files or different kinds of sources). 
 - [ ] Data splitting (training vs. test set): Here we only work with training data that is provided offline and only once. 
 - [x] Data exploration: Baby steps including seeing the column names, data types, etc.
 - [ ] Data exploration: Plots on each variable, the correlation between columns, etc. These should be included in the [documentation](documentation.html)
 - [x] Calculating replacements for missing values. This should be likely done for all variables even if nothing is missing in training data.
 - [x] Store replacement values in a [json](data/replacements.json) file.
 - [x] Preprocessing data (All the following are better to be independent even though they are included in the same method at the moment):
	 - [x] Imputing missing values (by using [json](data/replacements.json) produced before)
	 - [x] Feature engineering. 
	 - [x] Dropping unnecessary variables. 
 - [ ] Feature selection: Done manually, requires a method to automate the process. 
 - [x] Training model: 
	 - [x] Creation of the model 
	 - [ ] Storing the model in a pickle file (in an independent script/process)
 - [x] Evaluation of model: Choosing performance criteria
 	 - [x] Calculate performance metrics 
 	 - [ ] Store performance metrics for each model iteration in an independent script/process 
 - [x] An API endpoint to get new (raw) data points and provide a prediction

## Notes
-   Make every part of the project as independent as possible: (Combine than all in a shell script)
-   Store some data points at this point so after each iteration we know what is happening
-   Generalize this approach with the very simple initial model that will work any training data. So even the first version of the implementation should give predict some results (needless to say, nothing perfect) This also means that from the first time we deploy the algorithm, it will be available even if the results are not good at all
