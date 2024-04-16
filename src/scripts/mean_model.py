import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.optimizers import Adam

def load_data():
    '''
    Load the data and fit the encoders
    '''
    df = pd.read_csv('data/beer_reviews.csv')

    ndf = df[['review_profilename', 'beer_beerid', 'review_overall']]

    ndf.dropna()

    # Create a dictionary mapping beer IDs to names
    beer_id_to_name = pd.Series(df.beer_name.values, index=df.beer_beerid).to_dict()

   

    return ndf


def get_train_and_test_data(ndf):
    '''
    Split the data into training and testing sets
    '''
    # Split the dataset
    train, test = train_test_split(ndf, test_size=0.2, random_state=42)

    return train, test


def get_avg_rating(train):
    '''
    Get the average rating for each beer
    '''
    avg_rating = train.groupby('beer_beerid')['review_overall'].mean().reset_index()
    avg_rating.columns = ['beer_beerid', 'avg_rating']

    return avg_rating
def get_rating(username, beer_id, avg_rating):
    '''
    Get the rating for a beer
    '''
    # Check if the beer has an average rating
    if beer_id in avg_rating.beer_beerid.values:
        return avg_rating[avg_rating.beer_beerid == beer_id].avg_rating.values[0]
    else:
        return 0

def get_mae_and_rmse(predictions, test):
    '''
    Calculate MAE and RMSE
    '''
    # Calculate MAE
    mae = np.abs(predictions - test).mean()

    # Calculate RMSE
    rmse = np.sqrt(np.square(predictions - test).mean())

    return mae, rmse

def predic_test_set_using_mean_model(test, avg_rating):
    '''
    Predict the test set using the mean model
    '''
    predictions = []
    for index, row in test.iterrows():
        # Get the rating for the beer
        rating = get_rating(row['review_profilename'], row['beer_beerid'], avg_rating)
        predictions.append(rating)

    return predictions
def main():
    '''
    Main function
    '''
    ndf = load_data()
    print('a')
    train, test = get_train_and_test_data(ndf)
    print('b')
    avg_rating = get_avg_rating(train)
    print('c')
    predictions = predic_test_set_using_mean_model(test, avg_rating)
    print('d')
    test_ratings = test['review_overall'].values
    mae, rmse = get_mae_and_rmse(predictions, test_ratings)
    print(f"Mean Absolute Error: {mae}")
    print(f"Root Mean Squared Error: {rmse}")

if __name__ == '__main__':
    main()


    