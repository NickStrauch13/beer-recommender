import sys
sys.path.append('src/')
from scripts.model_utils import get_top_n_recommendations_NCF, get_user_list, get_top_n_recommendations_for_SVD
import pandas as pd

def get_recommendations_for_user(user, model_type, n=3):
    '''
    Get beer recommendations for a user
    params:
        user: str: username
        model_type: str: Model type to use for recommendations. One of ['SVD', 'NCF']
        n: int: Number of recommendations to return
    returns:
        list: List of beer recommendations
    '''
    # Load data
    df = pd.read_csv('data/beer_reviews.csv')
    ndf = df[['review_profilename', 'beer_beerid', 'review_overall', 'brewery_name', 'beer_style', 'beer_abv']]

    # Get recommendations
    if model_type == 'SVD':
        recommendations = get_top_n_recommendations_for_SVD(username=user, ndf=ndf, n=n, min_reviews=10)
    elif model_type == 'NCF':
        recommendations = get_top_n_recommendations_NCF(username=user, ndf=ndf, n=n, min_reviews=1)
    else:
        raise ValueError(f"Invalid model type {model_type}. Must be one of ['SVD', 'NCF']")
    
    # print(recommendations)
    # Convert recommendations to list of beer names
    recommendation_list = recommendations['beer_id'].tolist()
    recommendation_ratings = recommendations['predicted_rating'].tolist()
    # Get list of beer information
    beer_info = []
    # Load data
    df = pd.read_csv('data/beer_reviews.csv')
    for beer_id, pred_rating in zip(recommendation_list, recommendation_ratings):
        beer_info.append(get_beer_info(beer_id, pred_rating, df))
    return beer_info

def get_users():
    '''
    Get list of all users
    returns:
        list: List of all users
    '''
    # Load data
    df = pd.read_csv('data/beer_reviews.csv')
    return df['review_profilename'].unique()

def get_beer_info(beer_id, pred_rating, df):
    '''
    Get information about a beer
    params:
        beer_id: int: Beer ID
    returns:
        dict: Information about the beer
    '''
    
    beer_info_df = df[df['beer_beerid'] == beer_id]

    # Check if any entries are found
    if not beer_info_df.empty:
        beer_info = beer_info_df.iloc[0].to_dict()
        # Create a dictionary with only the required details
        beer_details = {
            'Beer Name': beer_info['beer_name'],
            'Brewery': beer_info['brewery_name'],
            'Beer Style': beer_info['beer_style'],
            'Predicted Rating': f"{pred_rating:.2f}",
        }
        return beer_details
    else:
        return None