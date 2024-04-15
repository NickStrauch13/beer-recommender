import sys
sys.path.append('src/')
from scripts.model_utils import get_top_n_recommendations_NCF, get_user_list, get_top_n_recommendations_for_SVD

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

    if model_type == 'SVD':
        return get_top_n_recommendations_for_SVD(user, ndf, n=n, min_reviews=10)

    elif model_type == 'NCF':
        return get_top_n_recommendations_NCF(user, ndf, n=n, min_reviews=1)
    
    else:
        raise ValueError(f"Invalid model type {model_type}. Must be one of ['SVD', 'NCF']")

def get_users():
    '''
    Get list of all users
    returns:
        list: List of all users
    '''
    return get_user_list()