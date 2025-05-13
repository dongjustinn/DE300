# Homework 2

This project answers three data analysis questions using Amazon Keyspaces (Cassandra) and data from hospital patient records. This assignment was divided into two parts -- relational and non-relational.

Requirements: Python, Cassandra, Boto3, Pandas, Jupyter Notebook, AWS, Docker, and CSV files listed below

CSV files:
'PATIENTS.csv'
'ADMISSIONS.csv'
'ICUSTAYS.csv'
'PROCEDURES_ICD.csv'
'D_ICD_PROCEDURES.csv'
'PRESCRIPTIONS.csv'

1. Start Jupyter
2. Forward the port from your local terminal
3. Upload the CSVs into the notebook session
4. The required SQL is executed using DuckDB:

```python
import duckdb

query = '''
SELECT subject_id, gender, ethnicity FROM patients
'''
duckdb.query(query).to_df()

For Part 1, Question 1, it will create a table of total quantity of medications by group and ranked by ethnicity.
For Part 1, Question 2, it will create an age calculated from date of birth and admission time. It will bin patients into 4 age groups. It will finally produce the top 3 procedures per age group.
For Part 1, Question 3, it will group by demographic to compute the average ICU stay to produce a table that shows average length of stay by gender and ethnicity.

For Part 2, it is run a little differently.

1. Launch Jupyter notebook in an EC2 instance.
2. Ensure AWS credentials are valid.
3. Connect to Amazon Keyspaces.

The code below is a sample code to help connect:
```python
from cassandra.auth import SigV4AuthProvider
from cassandra.cluster import Cluster
import boto3

boto_session = boto3.Session(...)
auth_provider = SigV4AuthProvider(boto_session)
cluster = Cluster(['cassandra.us-east-2.amazonaws.com'], port=9142, auth_provider=auth_provider)
session = cluster.connect()

For Part 2, Question 1, it will create a table de300.drug_by_ethnicity, which shows a table showing the top drug per group.
For Part 2, Question 2, there will be a list of the top 3 procedures by each age group. The data is stored in de300.patient_age_info.
For Part 2, Question 3, the output will be the average ICU length of stay by gender and ethnicity. The data is stored in de300.icu_stay_info.