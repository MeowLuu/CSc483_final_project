# CSc483_final_project

1. Data Loading and Inspection:
 - It reads JSON data from three different files (`business`, `user`, `review`) and stores them in Pandas DataFrames. These datasets represent business listings, user details, and user reviews on Yelp.
 - The business data is printed to inspect its structure after being loaded.

2. Data Handling in Chunks:
 - For both `user` and `review` data, it handles large datasets by processing them in chunks. This is useful for managing memory efficiently when working with very large datasets.

3. Category Extraction:
 - It extracts unique business categories from the `business` dataset. Each category from the `categories` column (which is a comma-separated string) is cleaned and added to a list if not already present.

4. String Matching Algorithm (Edit Distance):
 - A function called `edit_distance` calculates the Levenshtein distance between two words, which is a measure of the similarity between two strings. It's enhanced to also consider swaps of adjacent characters.

5. Encoding and Data Preprocessing:
 - The `preprocessing` function encodes several categorical columns using an `OrdinalEncoder`. This is typically done to convert categorical string data into a numerical format that can be used in machine learning algorithms.

6. Recommendation System:
 - The function `query` takes a user ID and a query string (a type of business category) as inputs. It then uses the user’s past review data to train a K-Nearest Neighbors classifier, predicting the user's potential ratings for businesses within the specified category.
 - It matches the user's query to the closest business category using the `edit_distance` function.
 - After identifying relevant businesses, it processes their data, predicts ratings using the trained model, and recommends the top businesses.
