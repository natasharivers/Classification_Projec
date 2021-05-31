# Telco Churn Classification Project

___________________________________________________________________________________
___________________________________________________________________________________

## Project Objectives

- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.

- Create modules (acquire.py, prepare.py) that make your process repeateable.

- Construct a model to predict customer churn using classification techniques.

- Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.

- Answer panel questions about your code, process, findings and key takeaways, and model.

___________________________________________________________________________________
___________________________________________________________________________________

## Business Goals

- Find drivers for customer churn at Telco.

- Construct a ML classification model that accurately predicts customer churn.

- Document your process well enough to be presented or read like a report.

___________________________________________________________________________________
___________________________________________________________________________________

## Audience

Codeup Data Science team

___________________________________________________________________________________
___________________________________________________________________________________

## Project Deliverables


- a Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation.

- a README.md file containing the project description with goals, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), key findings, recommendations, and takeaways from your project.

- a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn). These predictions should be from your best performing model ran on X_test. Note that the order of the y_pred and y_proba are numpy arrays coming from running the model on X_test. The order of those values will match the order of the rows in X_test, so you can obtain the customer_id from X_test and concatenate these values together into a dataframe to write to CSV.

- individual modules, .py files, that hold your functions to acquire and prepare your data.

- a notebook walkthrough presentation with a high-level overview of your project (5 minutes max). You should be prepared to answer follow-up questions about your code, process, tests, model, and findings.


___________________________________________________________________________________
___________________________________________________________________________________

## Data Dictionary

| Target |       Datatype        |    Definition      |
|--------|-----------------------|:------------------:|
| churn  | 7043 non-null: object |  yes or no         |


| Feature                 |       Datatype        |    Definition            |
|-------------------------|-----------------------|:------------------------:|
|senior_cititzen	      |7043 non-null: int64   |0 or 1 (boolean)          |
|tenure	                  |7043 non-null: int64   |in number of months       |
|monthly_charges	      |7043 non-null: float64 |USD cost per month        |

___________________________________________________________________________________
___________________________________________________________________________________

## Initial Hypothesis
- Hypothesis - I rejected the Null Hypothesis.
- alpha = .05
- H0: There is no relationship between churn and customer age 
- Ha: There is a relationshp between churn and customer age 

___________________________________________________________________________________
___________________________________________________________________________________

## Executive Summary- Conclusions & Next Steps
- My findings are:
    - I will be using the decision tree model as my best model for prediction my target value, churn because:
    - there is an accuracy of 79.36% on both the train set and 78.95% on the validate set
    - this model outperformed my baseline score of 73.12%
    - there is not a large drop off of accuracy between the two sets (thus it is not overfit)

- Given more time, I would:
    - I would run more models and change the hyperparameters on several different versions
    - I would look into adding surveying to exiting customers to further understand their actual cause of churn
    - We can then target the true reason to reduce churn in future customers
    - Use the new dataframe of predictions to target those specific customers that have the most potential to churn
    
___________________________________________________________________________________
___________________________________________________________________________________

## Pipeline Stages Breakdown

### --> Plan

- Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- Establish a baseline accuracy and document well.
- Train three different classification models.
- Evaluate models on train and validate datasets.
- Choose the model with that performs the best and evaluate that single model on the test dataset.
- Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.

### --> Acquire

- Store functions that are needed to acquire data from the telco database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
- The final function will return a pandas DataFrame.
- Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).

### --> Prepare 

- Store functions needed to prepare the telco data; make sure the module contains the necessary imports to run the code. The final function should do the following: - Split the data into train/validate/test. - Change data types as needed. - remove any duplicates. -change dataframe name 
- Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.


### --> Explore

- Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn.
- Run statistical test in data exploration. Document my hypotheses, set an alpha before running the test, and document the findings well.
- Create visualizations and run statistical test that work toward discovering variable relationships. The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. Run correlation code to identify if there is any positive correlation between churn and other variables.
- Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.

### --> Model 

- Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- Train (fit, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
- Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.


### --> Deliver

- Introduce myself and my project goals at the very beginning of my notebook walkthrough.
- Summarize my findings at the beginning like I would for an Executive Summary. 
- Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. 
- Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.
 
___________________________________________________________________________________
___________________________________________________________________________________

## Reproduce My Project

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

- Read this README.md
- Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- Add your own env file to your directory. (user, password, host)
- Run the final_report.ipynb notebook


___________________________________________________________________________________
___________________________________________________________________________________

## Other Resources

- Trello board: https://trello.com/b/g5ZLX2er/classification-project





