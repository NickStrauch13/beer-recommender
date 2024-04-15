import pandas as pd
from collections import defaultdict
from surprise import SVD, Dataset, Reader
import numpy as np
from keras.models import load_model
import joblib
import pickle

def get_top_n_recommendations_for_SVD(username,ndf, n=10, min_reviews=10, ):

    # load the model from the pickle file
    model = pickle.load(open('models/finalized_model.sav', 'rb'))
    df = pd.read_csv('data/beer_reviews.csv')
    # create beer_id to name dictionary
    beer_id_to_name = pickle.load(open('models/beer_id_to_name.sav', 'rb'))
    # beer_id_to_name = pd.Series(ndf.beer_name.values, index=ndf.beer_beerid).to_dict()
    # First, get all beer IDs that the user has not rated
    rated_beer_ids = ndf[ndf.review_profilename == username].beer_beerid.unique()
    all_beer_ids = ndf.beer_beerid.unique()
    unrated_beer_ids = list(set(all_beer_ids) - set(rated_beer_ids))

    # Next, predict the rating for each of these beers
    predictions = [model.predict(username, beer_id) for beer_id in unrated_beer_ids]

    # Get the top N predictions
    top_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)

    # Return the top N recommendations
    recommendations = defaultdict(list)
    for prediction in top_predictions:
        # Check if the beer has at least min_reviews reviews
        if ndf[ndf.beer_beerid == prediction.iid].shape[0] >= min_reviews:
            recommendations['beer_id'].append(prediction.iid)
            recommendations['beer_name'].append(beer_id_to_name[prediction.iid])
            recommendations['predicted_rating'].append(prediction.est)
        if len(recommendations['beer_id']) == n:
            break

    return pd.DataFrame(recommendations)


def get_top_n_recommendations_NCF(username,ndf, n=10, min_reviews=10):
    # load the model from the h5 file 
    model = load_model('models/ncf_model.h5')

    # load the user and item encoders from the pickle file
    user_encoder = joblib.load('models/user_encoder.pkl')
    item_encoder = joblib.load('models/item_encoder.pkl')
    ndf['user_encoded'] = user_encoder.fit_transform(ndf['review_profilename'])
    ndf['item_encoded'] = item_encoder.fit_transform(ndf['beer_beerid'])

    user_index = user_encoder.transform([username])[0]
    # num_users = ndf['user_encoded'].nunique()
    num_items = ndf['item_encoded'].nunique()
    # Create a list of all beer indices
    all_beer_indices = np.arange(num_items)

    beer_id_to_name = pickle.load(open('models/beer_id_to_name.sav', 'rb'))
    
    # Remove the beers that the user has already rated
    beers_rated = ndf[ndf['user_encoded'] == user_index]['item_encoded'].values
    beers_unrated = np.setdiff1d(all_beer_indices, beers_rated)

    # Filter out beers with less than min_reviews reviews
    beer_review_counts = ndf['item_encoded'].value_counts()
    beers_unrated = np.array([beer_id for beer_id in beers_unrated if beer_review_counts[beer_id] >= min_reviews])

    # Make a prediction for the user on all unrated beers
    user_indices = np.array([user_index] * len(beers_unrated))
    predictions = model.predict([user_indices, beers_unrated])

    # Get the indices that would sort the predictions array
    sorted_indices = np.argsort(predictions, axis=0)[::-1].flatten()

    # Get the top N recommendations
    top_n_indices = beers_unrated[sorted_indices][:n]

    # Convert the beer indices back to beer IDs
    top_n_beer_ids = item_encoder.inverse_transform(top_n_indices)

    # Get the beer names using the IDs
    top_n_beer_names = [beer_id_to_name[beer_id] for beer_id in top_n_beer_ids]
    
    # return the top n predictions

    top_n_predictions = [predictions[i] for i in sorted_indices[:n]]

    # make top n predictions into a list
    top_n_predictions = [x[0] for x in top_n_predictions]
    # make dataframe of the top n recommendations with the beer names and predicted ratings
    df = pd.DataFrame({'beer_id': top_n_beer_ids, 'beer_name': top_n_beer_names, 'predicted_rating': top_n_predictions})
    return df

def get_user_list(ndf):
    '''
    Get a list of all users in the dataset
    '''
    return ndf['review_profilename'].unique()


