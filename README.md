# Classification_Project


## Project Objectives

- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.

- Create modules (acquire.py, prepare.py) that make your process repeateable.

- Construct a model to predict customer churn using classification techniques.

- Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.

- Answer panel questions about your code, process, findings and key takeaways, and model.

___________________________________________________________________________________

## Business Goals

- Find drivers for customer churn at Telco.

- Construct a ML classification model that accurately predicts customer churn.

- Document your process well enough to be presented or read like a report.

___________________________________________________________________________________

## Audience

Codeup Data Science team

___________________________________________________________________________________

## Deliverables


- a Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation.

- a README.md file containing the project description with goals, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), key findings, recommendations, and takeaways from your project.

- a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn). These predictions should be from your best performing model ran on X_test. Note that the order of the y_pred and y_proba are numpy arrays coming from running the model on X_test. The order of those values will match the order of the rows in X_test, so you can obtain the customer_id from X_test and concatenate these values together into a dataframe to write to CSV.

- individual modules, .py files, that hold your functions to acquire and prepare your data.

- a notebook walkthrough presentation with a high-level overview of your project (5 minutes max). You should be prepared to answer follow-up questions about your code, process, tests, model, and findings.

___________________________________________________________________________________

## Data Dictionary

| Target |       Datatype        |    Definition    |
|--------|-----------------------|------------------|
| churn  | 7043 non-null: object | churn: yes or no |



Feature	Datatype	Definition
gender	7043 non-null: object	0 or 1
senior_cititzen	7043 non-null: int64	0 or 1
partner	7043 non-null: object	0 or 1
dependents	7043 non-null: object	0 or 1
tenure	7043 non-null: int64	 in number of months
phone_service	7043 non-null: object	0, 1 or 2
multiple_lines	7043 non-null: object	0 or 1
internet_service_type_id	7043 non-null: int64	0 or 1
online_security	7043 non-null: object	0 or 1
online_backup	7043 non-null: object	0 or 1
device_protection	7043 non-null: object	0 or 1
tech_support	7043 non-null: object	0 or 1
streaming_tv	7043 non-null: object	0 or 1
streaming_movies	7043 non-null: object	0 or 1
contract_type_id	7043 non-null: int64	0 or 1
paperless_billing	7043 non-null: object	0 or 1
payment_type_id	7043 non-null: int64	0 or 1
monthly_charges	7043 non-null: float64	USD cost per month
total_charges	7043 non-null: object	USD cost total
contract_type_id	7043 non-null: int64	0, 1 or 2
contract_type	7043 non-null: object	explains type of plan
payment_type_id	7043 non-null: int64	0, 1 or 2
payment_type	7043 non-null: object	explains type of plan
internet_service_type_id	7043 non-null: int64	0, 1 or 2
internet_service_type	7043 non-null: object	explains type of plan


