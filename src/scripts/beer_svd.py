import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split, cross_validate
from surprise import accuracy
df = pd.read_csv('../../data/beer_reviews.csv')

ndf = df[['review_profilename', 'beer_beerid', 'review_overall']]
ndf = ndf.dropna() 


# Create a dictionary mapping beer IDs to names
beer_id_to_name = pd.Series(df.beer_name.values,index=df.beer_beerid).to_dict()

# Prepare the DataFrame for Surprise
reader = Reader(rating_scale=(0, 5))
data = Dataset.load_from_df(ndf[['review_profilename', 'beer_beerid', 'review_overall']], reader)

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.25, random_state=42)

# Train the SVD model
model = SVD()
model.fit(trainset)
predictions = model.test(testset)

# Calculate and print RMSE
accuracy.rmse(predictions)

# Cross-validation
results = cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
print(f"Cross validation: {results}")


