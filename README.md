Homework 1

This contains Homework 1 for DE300. The goal of this homework was to do comprehensive data cleaning, transformation, and overall clean-up for the airline dataset T_F41SCHEDULE_B43.csv.

To run this file, make sure that T_F41SCHEDULE_B43.csv is in the same directory that you are trying to run the code. You can run the script of the code, which is titled DE300_HW1.py, by running "python DE300_HW1.py". This will execute all of the steps in the code. This includes, but isn't limited to, missing data analysis and imputation steps for the "CARRIER," "CARRIER_NAME," "MANUFACTURE_YEAR," "NUMBER_OF_SEATS," "CAPACITY_IN_POUNDS," and "AIRLINE_ID" columns. This compares mean, median, KNN, and PMM imputation for a few of these columns, with root mean squared error (RMSE) being the key for comparison.

The code also will standardize and transform select columns. The columns in question are "MANUFACTURER," "MODEL," "AIRCRAFT_STATUS," and "OPERATING_STATUS." This makes sure that there are as little redundancies as possible by readjusting some of the data entries.

After this, all rows with missing values still will be dropped, and the remaining row count will be printed. 

Following this, a Box-Cox transformation of "NUMBER_OF_SEATS" and "CAPACITY_IN_POUNDS" will be performed. Histograms of before and after this transformation will be shown as well.

Finally, the code performs a little bit of feature performing, by creating a "SIZE" quartile column and plotting the proportions of operating vs. non-operating and aircraft status by these size quartiles.

THe expected outputs should be a cleaned up .csv file. There will be RMSE values for each imputation method attempted, counts of unique cleaned categories, and the number of rows remainings after dropped missing data. The plots that are generated include histogrames of "NUMBER_OF_SEATS" and "CAPACITY_IN_POUNDS" before and after Box-Cox, bar charts of operating status proportionally by size quartile, and bar charts of aircraft status proportionally by size quartile.