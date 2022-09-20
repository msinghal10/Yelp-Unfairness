The Final Dataset csv, contains 8 columns, all labeled with their respective headings. This is the final dataset that was formed after filtering out all the "Removed reviews" from the dataset. 

The yelp-scraper code, collects all the not recommended reviews for the given business. A test file is provided as to help in creating the businesses. You can change the code accordingly to get what is required. Make sure the cookies are changed each time you collect the data, you can get that information from the Network tab in the browser. 

The batch-new-add file gives the syntax of how yelp wants the business name to go through its system.

The remove-extraheader.py file will help in cleaning the dataset. You need to merge all the csv together. Easiest way is to run the following command in the folder that you have "cat *.csv > Total-reviews.csv" Once you have done this step, run the python file to get cleaned dataset.
