# Telco Churn Classification Project


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

| Target |       Datatype        |    Definition      |
|--------|-----------------------|:------------------:|
| churn  | 7043 non-null: object |  yes or no         |


| Feature                 |       Datatype        |    Definition            |
|-------------------------|-----------------------|:------------------------:|
|gender                   |7043 non-null: object  | Female or Male           |
|senior_cititzen	      |7043 non-null: int64   |0 or 1 (boolean)          |
|partner	              |7043 non-null: object  |Yes or No                 |
|dependents	              |7043 non-null: object  |Yes or No                 |
|tenure	                  |7043 non-null: int64   |in number of months       |
|phone_service	          |7043 non-null: object  |Yes or No                 |
|multiple_lines	          |7043 non-null: object  |Yes, No phone service, No |
|internet_service_type_id |7043 non-null: int64   |1, 2, or 3                |
|online_security	      |7043 non-null: object  |Yes or No                 |
|online_backup	          |7043 non-null: object  |Yes or No                 |
|device_protection	      |7043 non-null: object  |Yes or No                 |
|tech_support	          |7043 non-null: object  |Yes or No                 |
|streaming_tv	          |7043 non-null: object  |Yes or No                 |
|streaming_movies	      |7043 non-null: object  |Yes or No                 |
|contract_type_id	      |7043 non-null: int64   |1, 2, or 3                |
|paperless_billing	      |7043 non-null: object  |Yes or No                 |
|payment_type_id	      |7043 non-null: int64   |1, 2, 3 or 4              |
|monthly_charges	      |7043 non-null: float64 |USD cost per month        |
|total_charges	          |7043 non-null: object  |USD cost total            |
|contract_type_id	      |7043 non-null: int64   |1, 2, or 3                |
|contract_type	          |7043 non-null: object  |explains type of plan     |
|payment_type	          |7043 non-null: object  |explains type of plan     |
|internet_service_type_id |7043 non-null: int64   |1, 2 or 3                 |
|internet_service_type	  |7043 non-null: object  |explains type of plan     |



___________________________________________________________________________________

## Reproducibility

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

- Read this README.md
- Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- Add your own env file to your directory. (user, password, host)
- Run the final_report.ipynb notebook


___________________________________________________________________________________

## Other resources

- Trello board: https://trello.com/b/g5ZLX2er/classification-project
- Canva Customer Retenetion Project: https://www.canva.com/design/DAEdbr4_q_k/share/preview?token=4GETfzg3CIZCyWowl9x88A&role=EDITOR&utm_content=DAEdbr4_q_k&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton


