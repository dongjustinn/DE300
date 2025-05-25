# DATAENG 300 — Homework 3

This project applies MapReduce concepts using PySpark to complete two major tasks:

1. Compute tf-idf scores for a collection of news articles.
2. Evaluate the objective function for a linear Support Vector Machine (SVM) using custom MapReduce logic.

## Part 0: Quick Start

Create and activate a fresh environment. You can do this with any name!
python -m venv venv
source venv/bin/activate

Install dependencies. You may find you need to download more if it asks you to.
pip install pyspark==3.5.1 pandas numpy

Launch Jupyter and run all cells.
jupyter notebook DE300HW3.ipynb

## Part 1: tf-idf on AG News Data

I used PySpark RDD transformations to calculate tf-idf values from the AG News dataset. This involved:
- Computing term frequency (TF) for each word in each document.
- Computing document frequency (DF) across the corpus.
- Applying the tf-idf formula manually with MapReduce logic.
The final tf-idf results were added as a new column and previewed in the output.

The final results of this section should be the tf-idf measure for each row in the agnews_clean.csv. There should also be a printed table of the td-idf measure for the first 5 documents.

## Part 2: SVM Objective and Prediction with MapReduce

Using distributed processing, I evaluated the soft-margin SVM loss function:
- Input data: `data_for_svm.csv`, `w.csv`, and `bias.csv`.
- The loss function includes both hinge loss and L2 regularization:
  
  Objective = (1/n) * sum(max(0, 1 - yᵢ(wᵗxᵢ + b))) + λ * ||w||²

- I used numpy operations to compute:
  - The average hinge loss across all rows.
  - The regularization term using the L2 norm of the weight vector.
- Predictions were generated using the sign of (wᵗx + b).

The final outputs of this section should be the objective value using the weights and bias provided using the function loss_SVM created. There should also be a prediction for all of the data, with some of the first few examples being shown.

## Technologies

- Python 3
- PySpark (RDD API only — no MLlib)

## Notes

- All calculations and predictions were implemented manually using RDD logic to follow a MapReduce paradigm.
- This homework reinforced Spark fundamentals and showed how large-scale machine learning computations can be broken down into basic operations.

## Final Outputs

DE300HW3.ipynb - This is the main homework notebook. It contains the code for parts 1 and 2.
dataset/ - This folder was created explicitly in the code. Data files were downloaded into this using !curl. This contains the input data for part 1.
dataset/tfidf_output/ - This subfolder is the output folder for my tf-idf results.
data_for_svm.csv - This was downloaded from the code.
w.csv - This was downloaded from the code.
bias.csv - This was downloaded from the code.