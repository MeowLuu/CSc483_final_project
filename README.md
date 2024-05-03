# CSc483_final_project
# Yelp Data Analysis and Recommendation System
- Submission Day : May 1 2024

# Project Goal
This project develops a personalized recommendation system using Yelp's dataset, analyzing user reviews and business categories. It employs machine learning to predict user preferences based on historical ratings, recommending businesses by matching user queries to similar categories through a sophisticated string matching algorithm.

# Authors
- Hayden Arnold
- Nick Avalani
- Selina Lu

# Files
- `src/project/Project.ipynb`


# Functionality
1. Data Loading and Inspection

- Business Data: Load business data from a JSON file (yelp_academic_dataset_business.json), which includes details like business names, addresses, and categories.
- User Data: Load user data from a JSON file (yelp_academic_dataset_user.json), containing user details.
- Review Data: Load review data from a JSON file (yelp_academic_dataset_review.json), which includes user-generated reviews on businesses.
- Each dataset is loaded into Pandas DataFrames, allowing for easy data manipulation and analysis.

  Please note that all three files are downloadable from the dataset (https://www.yelp.com/dataset), but that only a fraction of the data was used here, as the files exceed 20gb in total.

2. Data Handling in Chunks

The script processes user and review data in chunks to manage memory efficiently, suitable for handling large datasets without overwhelming system memory. Each chunk is processed sequentially until the specified total number of records has been reached.

3. Category Extraction

Extracts and cleans unique business categories from the business dataset. This involves splitting category strings, stripping extra spaces, and ensuring uniqueness.

4. Encoding and Data Preprocessing

Converts categorical data into a numerical format using OrdinalEncoder. This includes encoding business names, addresses, cities, states, postal codes, and categories, making the data suitable for machine learning algorithms.

5. Similarity Calculation

Uses the SentenceTransformer library to calculate the cosine similarity between a user's text query and the available categories, helping to identify the most relevant business category related to the query.

6. Recommendation System

Query Function: Accepts a user ID and a text query (business type/category). It first checks if the user has enough reviews for reliable predictions. If valid, it trains a K-Nearest Neighbors classifier using the user's past review data and predicts potential ratings for businesses within the queried category.
Output: Displays the top recommended businesses based on the predicted ratings, ordered by relevance and rating.

# Resourse/Reference 
- [yelp database] (https://www.yelp.com/dataset)


# Usage
To run the recommendation system:

Ensure all dependencies are installed.
Run the script section by section, beginning with data loading and moving through preprocessing and querying.
Input a user ID and a query term to receive business recommendations. An optional test flag is included if accuracy testing is needed.

# Dependencies
- Python 3.8+
- Pandas
- Scikit-Learn
- Sentence Transformers
- JSON
